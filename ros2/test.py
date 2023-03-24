import json
import pickle
from tensorflow import keras
import os
import tensorflow as tf
from tensorflow import keras
import random
from copy import copy
import numpy as np
class Utils:
    @staticmethod
    def save_json(path, data):
        with open(path, "w+") as out:
            data = json.dumps(data)
            out.write(data)

    @staticmethod
    def save_pickle(path, data):
        with open(path, "wb+") as file:
            pickle.dump(data, file)

    @staticmethod
    def load_json(path, type):

        with open(path) as outfile:
            param = json.load(outfile)

            return param.get(type)

    @staticmethod
    def load_pickle(path):

        with open(path, 'rb') as file:
            return pickle.load(file)

    @staticmethod
    def save_model(model, path):
        model.save(path)

    @staticmethod
    def load_model(model, path):
        model.set_weights(keras.models.load_model(path).get_weights())
        return model

loss_function = keras.losses.Huber()
def create_model() -> keras.Model:
        # initializer1 = tf.keras.initializers.GlorotNormal()

        # initializer2 = tf.keras.initializers.GlorotNormal()

        inputs = keras.layers.Input(shape=(3,))

        out = keras.layers.Dense(
            128, activation="relu", kernel_initializer='glorot_normal')(inputs)

        out = keras.layers.Dropout(0.2)(out)
        out = keras.layers.Dense(
            128,  activation="relu" ,kernel_initializer='glorot_normal')(out)
        out = keras.layers.Dropout(0.2)(out)
        
        action = keras.layers.Dense(
            5, activation="linear")(out)

        return keras.Model(inputs=inputs, outputs=action)
model=create_model()
target_model=model
dir_path = os.path.dirname(os.path.realpath(__file__))
replay_memory=Utils.load_pickle()
optimizer = keras.optimizers.Adam(learning_rate=0.0001) 

def train(self, terminal_state):
        
    
        minibatch = random.sample(replay_memory, 64)

        current_states = tf.convert_to_tensor(np.array([batch[0] for batch in minibatch]))
        rewards = tf.convert_to_tensor(np.array([batch[1] for batch in minibatch]))
        rewards = tf.cast(rewards, dtype=tf.float32)
        actions = tf.convert_to_tensor(np.array([batch[2] for batch in minibatch]))
        next_states = tf.convert_to_tensor(np.array([batch[3] for batch in minibatch]))
        dones =tf.convert_to_tensor( np.array([float(batch[4]) for batch in minibatch]))
        dones = tf.cast(dones, dtype=tf.float32)
        next_q_values = target_model(next_states,training=True)
        
        updated_q_values = rewards+0.99 * \
            tf.reduce_max(next_q_values, axis=1)*(1.0-dones)
        masks = tf.one_hot(actions, 5)
       
        with tf.GradientTape() as tape:
            # Train the model on the states and updated Q-values
            q_values = model(current_states,training=True)

            # Apply the masks to the Q-values to get the Q-value for action taken
            q_action = tf.reduce_sum(tf.multiply(q_values, masks), axis=1)
            
            # Calculate loss between new Q-value and old Q-value
            loss = loss_function(updated_q_values, q_action)
            

            # Backpropagation
            grads = tape.gradient(loss, model.trainable_variables)
            optimizer.apply_gradients(
                zip(grads, model.trainable_variables))

        if terminal_state:
            target_update_counter += 1

        # If counter reaches set value, update target network with weights of main network
        if target_update_counter > 5:
            target_model.set_weights(model.get_weights())
            target_update_counter = 0
def load_data():
        model = create_model()
        path = os.path.join(dir_path, get_model_file_name("h5"))
        model = Utils.load_model(model, path)

        path = os.path.join(dir_path, get_model_file_name("json"))
        epsilon = Utils.load_json(path, "epsilon")
        path = os.path.join(dir_path, get_model_file_name("obj"))
        replay_memory = Utils.load_pickle(path)



def save_data(self, ep, epsilon,reward):
        ep = ep
        path = os.path.join(dir_path, get_model_file_name("h5"))
        to_save = copy(model)
        to_save.compile(optimizer=optimizer, loss=loss_function)
        Utils.save_model(to_save, path)
        path = os.path.join(dir_path, get_model_file_name("json"))
        data = {"epsilon": epsilon,"reward":reward}
        Utils.save_json(path, data)
        path = os.path.join(dir_path, get_model_file_name("obj"))
        Utils.save_pickle(path, replay_memory)

def get_model_file_name(self, type):
        return f"my-model-300.{type}"


