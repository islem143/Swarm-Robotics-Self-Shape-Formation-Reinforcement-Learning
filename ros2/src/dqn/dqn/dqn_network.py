from tensorflow import keras
import tensorflow as tf
from collections import deque
from .utils import Utils
import numpy as np
import random
from dqn_msg.srv import Dqnn
from std_srvs.srv import Empty
import psutil
import time
import rclpy
import os
from copy import copy

from rclpy.node import Node
physical_devices = tf.config.list_physical_devices('GPU')
try:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
except:
    # Invalid device or cannot modify virtual devices once initialized.
    pass
optimizer = keras.optimizers.Adam(learning_rate=0.00025, clipnorm=1.0)

loss_function = keras.losses.Huber()


class Network:

    def __init__(self, name, model_load=False, ep=0) -> None:
        self.name = name
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        if (model_load):
            self.ep = ep
            self.load_data()

        else:
            self.model = self.create_model()
            self.epsilon = 1
            self.replay_memory = deque(maxlen=50_000)
            self.ep = ep

        # to note we are having the same target of if we load the model
        self.target_model = self.model
        self.actions = [-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2]
        self.actions_size = 5
        self.state_size = 3
        self.discout_factor = 0.99
        self.minbatch_size = 64
        self.MIN_REPLAY_MEMORY_SIZE = 1000

        self.target_update_counter = 0

    def create_model(self) -> keras.Model:
        initializer1 = tf.keras.initializers.HeNormal()
        initializer2 = tf.keras.initializers.HeNormal()
        inputs = keras.layers.Input(shape=(3,))

        layer1 = keras.layers.Dense(
            1024, activation=keras.layers.LeakyReLU(), kernel_initializer=initializer1)(inputs)

        dropout = keras.layers.Dropout(0.2)(layer1)
        layer2 = keras.layers.Dense(
            1024,  activation=keras.layers.LeakyReLU(), kernel_initializer=initializer2)(dropout)
        action = keras.layers.Dense(
            5, activation="linear")(layer2)

        return keras.Model(inputs=inputs, outputs=action)

    def get_action(self, state):

        state = np.array(state, dtype=np.float64)
        state = tf.expand_dims(tf.convert_to_tensor(state), 0)

        return self.model.predict(state, verbose=0)

    def update_replay_buffer(self, sample):
        self.replay_memory.append(sample)

    def train(self, terminal_state):
        if (self.MIN_REPLAY_MEMORY_SIZE > len(self.replay_memory)):
            return

        minibatch = random.sample(self.replay_memory, self.minbatch_size)

        current_states = np.array([batch[0] for batch in minibatch])
        rewards = np.array([batch[1] for batch in minibatch])
        actions = np.array([batch[2] for batch in minibatch])
        next_states = np.array([batch[3] for batch in minibatch])
        next_q_values = self.target_model.predict(next_states, verbose=0)
        dones = np.array([float(batch[4]) for batch in minibatch])
        updated_q_values = rewards+self.discout_factor * \
            np.max(next_q_values, axis=1)*(1.0-dones)
        masks = tf.one_hot(actions, self.actions_size)

        with tf.GradientTape() as tape:
            # Train the model on the states and updated Q-values
            q_values = self.model(current_states)

            # Apply the masks to the Q-values to get the Q-value for action taken
            q_action = tf.reduce_sum(tf.multiply(q_values, masks), axis=1)
            # Calculate loss between new Q-value and old Q-value
            loss = loss_function(updated_q_values, q_action)

            # Backpropagation
            grads = tape.gradient(loss, self.model.trainable_variables)
            optimizer.apply_gradients(
                zip(grads, self.model.trainable_variables))

        if terminal_state:
            self.target_update_counter += 1

        # If counter reaches set value, update target network with weights of main network
        if self.target_update_counter > 5:
            self.target_model.set_weights(self.model.get_weights())
            self.target_update_counter = 0

    def load_data(self):
        model = self.create_model()
        path = os.path.join(self.dir_path, self.get_model_file_name("h5"))
        self.model = Utils.load_model(model, path)

        path = os.path.join(self.dir_path, self.get_model_file_name("json"))
        self.epsilon = Utils.load_json(path, "epsilon")
        path = os.path.join(self.dir_path, self.get_model_file_name("obj"))
        self.replay_memory = Utils.load_pickle(path)

    def get_epsilon(self):
        return self.epsilon

    def save_data(self, ep, epsilon):
        self.ep = ep
        path = os.path.join(self.dir_path, self.get_model_file_name("h5"))
        to_save = copy(self.model)
        to_save.compile(optimizer=optimizer, loss=loss_function)
        Utils.save_model(to_save, path)
        path = os.path.join(self.dir_path, self.get_model_file_name("json"))
        data = {"epsilon": epsilon}
        Utils.save_json(path, data)
        path = os.path.join(self.dir_path, self.get_model_file_name("obj"))
        Utils.save_pickle(path, self.replay_memory)

    def get_model_file_name(self, type):
        return f"models-{self.name}/my-model-{self.ep}.{type}"
