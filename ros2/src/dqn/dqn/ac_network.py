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

loss_function = keras.losses.Huber()


class ACNetwork():
    def __init__(self, name, model_load=False, ep=0) -> None:
        self.name = name
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.upper_bound=1.5  
        self.lower_bound=-1.5 
        self.critic_lr = 0.00025
        self.actor_lr = 0.00015
        self.critic_optimizer = tf.keras.optimizers.Adam(learning_rate=self.critic_lr)
        self.actor_optimizer = tf.keras.optimizers.Adam(learning_rate=self.actor_lr)
       
        if (model_load):
            self.ep = ep
            self.load_data()
          
        else:
            #self.model = self.create_model()
            self.actor_model = self.create_actor_model()
            self.critic_model = self.create_critic_model()

            self.target_actor = self.create_actor_model()
            self.target_critic = self.create_critic_model()

  
            #self.replay_memory = deque(maxlen=100_000)
            self.buffer_counter = 0
            self.buffer_capacity=100_000
            # Instead of list of tuples as the exp.replay concept go
            # We use different np.arrays for each tuple element
            self.state_buffer = np.zeros((self.buffer_capacity, 3))
            self.action_buffer = np.zeros((self.buffer_capacity,1))
            self.reward_buffer = np.zeros((self.buffer_capacity, 1))
            self.next_state_buffer = np.zeros((self.buffer_capacity,3))
            self.dones = np.zeros((self.buffer_capacity,1))
            self.ep = ep
            
        ep_rewards=[]  
       
        #learning_rate=0.00025
        
        # to note we are having the same target of if we load the model
      
      

        self.state_size = 3
        self.discout_factor = 0.99
        self.minbatch_size = 500
        self.MIN_REPLAY_MEMORY_SIZE =64
      

       

        self.target_update_counter = 0

    def create_actor_model(self):
        # Initialize weights between -3e-3 and 3-e3
        last_init = tf.random_uniform_initializer(minval=-0.0003, maxval=0.0003)


        inputs = keras.layers.Input(shape=(3,))
        out = keras.layers.Dense(512, activation="relu",kernel_initializer="he_normal")(inputs)
        out=keras.layers.Dropout(0.5)(out)
        out = keras.layers.BatchNormalization()(out)
        out = keras.layers.Dense(512, activation="relu",kernel_initializer="he_normal")(out)
        out=keras.layers.Dropout(0.5)(out)
        out = keras.layers.BatchNormalization()(out)
        out = keras.layers.Dense(512, activation="relu",kernel_initializer="he_normal")(out)
        out=keras.layers.Dropout(0.5)(out)
        out = keras.layers.BatchNormalization()(out)
        out = keras.layers.Dense(512, activation="relu",kernel_initializer="he_normal")(out)
        out=keras.layers.Dropout(0.5)(out)
        out = keras.layers.BatchNormalization()(out)
        outputs = keras.layers.Dense(1, activation="tanh",kernel_initializer=last_init)(out)

        
        outputs = outputs * self.upper_bound
        model = tf.keras.Model(inputs, outputs)
        return model
    
    def create_critic_model(self):
        last_init = tf.random_uniform_initializer(minval=-0.0003, maxval=0.003)
        state_input = keras.layers.Input(shape=(3))
        state_out = keras.layers.Dense(16, activation="relu",kernel_initializer="he_normal")(state_input)
        state_out = keras.layers.BatchNormalization()(state_out)
        state_out = keras.layers.Dense(32, activation="relu",kernel_initializer="he_normal")(state_out)
        state_out = keras.layers.BatchNormalization()(state_out)

            # Action as input
        action_input = keras.layers.Input(shape=(1))
        action_out = keras.layers.Dense(32, activation="relu",kernel_initializer="he_normal")(action_input)
        action_out =  keras.layers.BatchNormalization()(action_out)
            # Both are passed through seperate layer before concatenating
        concat = keras.layers.Concatenate()([state_out, action_out])

        out = keras.layers.Dense(512, activation="relu",kernel_initializer="he_normal")(concat)
        out=keras.layers.Dropout(0.5)(out)
        out = keras.layers.BatchNormalization()(out)
        out = keras.layers.Dense(512, activation="relu",kernel_initializer="he_normal")(out)
        out=keras.layers.Dropout(0.5)(out)
        out = keras.layers.BatchNormalization()(out)
        out = keras.layers.Dense(512, activation="relu",kernel_initializer="he_normal")(out)
        out=keras.layers.Dropout(0.5)(out)
        out = keras.layers.BatchNormalization()(out)
        out = keras.layers.Dense(512, activation="relu",kernel_initializer="he_normal")(out)
        out=keras.layers.Dropout(0.5)(out)
        out = keras.layers.BatchNormalization()(out)
        outputs = keras.layers.Dense(1,kernel_initializer="he_normal")(out)

        # Outputs single value for give state-action
        model = tf.keras.Model([state_input, action_input], outputs)

        return model

    def policy(self,state, noise_object):
        print(state)
        sampled_actions = tf.squeeze(self.actor_model(state))
        print("samlple",sampled_actions)
        noise = noise_object()
        
        # Adding noise to action
        sampled_actions = sampled_actions.numpy() + 0
         
        # We make sure action is within bounds
        legal_action = np.clip(sampled_actions, self.lower_bound, self.upper_bound)
        print(legal_action)

        return [np.squeeze(legal_action)]
    @tf.function
    def update(
        self, state_batch, action_batch, reward_batch, next_state_batch,dones
    ):
            # Training and updating Actor & Critic networks.
            # See Pseudo Code.
            
            with tf.GradientTape() as tape:
                target_actions = self.target_actor(next_state_batch, training=True)
               
                y = reward_batch + self.discout_factor * self.target_critic(
                    [next_state_batch, target_actions], training=True
                )
                
                
                critic_value = self.critic_model([state_batch, action_batch], training=True)
                critic_loss = tf.math.reduce_mean(tf.math.square(y - critic_value))

               

            critic_grad = tape.gradient(critic_loss, self.critic_model.trainable_variables)
            self.critic_optimizer.apply_gradients(
                zip(critic_grad, self.critic_model.trainable_variables)
            )

            with tf.GradientTape() as tape:
                actions = self.actor_model(state_batch, training=True)
                critic_value = self.critic_model([state_batch, actions], training=True)
                # Used `-value` as we want to maximize the value given
                # by the critic for our actions
                actor_loss = -tf.math.reduce_mean(critic_value)
         

            actor_grad = tape.gradient(actor_loss, self.actor_model.trainable_variables)
            self.actor_optimizer.apply_gradients(
                zip(actor_grad, self.actor_model.trainable_variables)
            )

    @tf.function
    def update_target(self,target_weights, weights, tau):
  
     for (a, b) in zip(target_weights, weights):
        a.assign(b * tau + a * (1 - tau))

    def update_replay_buffer(self, sample):
        self.buffer_counter+=1

        index = self.buffer_counter % self.buffer_capacity

        self.state_buffer[index] = sample[0]
        self.reward_buffer[index] = sample[1]
        self.action_buffer[index] = sample[2]
        self.next_state_buffer[index] = sample[3]
        self.dones[index]=sample[4]

    def learn(self):
        if (self.MIN_REPLAY_MEMORY_SIZE > self.buffer_counter):
            return
        
        # mean=np.mean(np.array(self.replay_memory,dtype=np.float32),axis=1)
        # std = np.std(np.array(self.replay_memory,dtype=np.float32), axis=1)
        # print("mean",std)  
     
        record_range = min(self.buffer_counter, self.buffer_capacity)
        # Randomly sample indices
        batch_indices = np.random.choice(record_range, self.minbatch_size)
   
        # Convert to tensors
        state_batch = tf.convert_to_tensor(self.state_buffer[batch_indices])
        action_batch = tf.convert_to_tensor(self.action_buffer[batch_indices])
        reward_batch = tf.convert_to_tensor(self.reward_buffer[batch_indices])
        reward_batch = tf.cast(reward_batch, dtype=tf.float32)
        next_state_batch = tf.convert_to_tensor(self.next_state_buffer[batch_indices])
        dones = tf.convert_to_tensor(self.dones[batch_indices])
        
        self.update(state_batch, action_batch, reward_batch, next_state_batch,dones)

    def load_data(self):
        self.actor_model = self.create_actor_model()
        self.target_actor = self.create_actor_model()
        self.critic_model = self.create_critic_model()
        self.target_critic = self.create_critic_model()
        path1 = os.path.join(self.dir_path, self.get_model_file_name("h5","actor"))
        path2 = os.path.join(self.dir_path, self.get_model_file_name("h5","target-actor"))
        path3 = os.path.join(self.dir_path, self.get_model_file_name("h5","critic"))
        path4 = os.path.join(self.dir_path, self.get_model_file_name("h5","target-critic"))
        self.actor_model = Utils.load_model(self.actor_model, path1)
        self.target_actor = Utils.load_model(self.target_actor, path2)
        self.critic_model = Utils.load_model(self.critic_model, path3)
        self.target_critic = Utils.load_model(self.target_critic, path4)

    
        # path = os.path.join(self.dir_path, self.get_model_file_name("obj","None"))
        # self.replay_memory = Utils.load_pickle(path)

    def get_epsilon(self):
        return self.epsilon

    def save_data(self, ep,reward):
        self.ep = ep
        path1 = os.path.join(self.dir_path, self.get_model_file_name("h5","actor"))
        path2 = os.path.join(self.dir_path, self.get_model_file_name("h5","target-actor"))
        path3 = os.path.join(self.dir_path, self.get_model_file_name("h5","critic"))
        path4 = os.path.join(self.dir_path, self.get_model_file_name("h5","target-critic"))
        actor = copy(self.actor_model)
        target_actor = copy(self.target_actor)
        critic = copy(self.critic_model)
        target_critic = copy(self.target_critic)
        #fix this the loss function
        actor.compile(optimizer=self.actor_optimizer, loss=loss_function)
        target_actor.compile(optimizer=self.actor_optimizer, loss=loss_function)
        critic.compile(optimizer=self.critic_optimizer, loss=loss_function)
        target_critic.compile(optimizer=self.critic_optimizer, loss=loss_function)
        Utils.save_model(actor, path1)
        Utils.save_model(target_actor, path2)
        Utils.save_model(critic, path3)
        Utils.save_model(target_critic, path4)
        path = os.path.join(self.dir_path, self.get_model_file_name("json"))
        data = {"reward":reward}
        Utils.save_json(path, data)
       
        # path = os.path.join(self.dir_path, self.get_model_file_name("obj"))
        # Utils.save_pickle(path, self.replay_memory)

    def get_model_file_name(self, type,ext=None):
        return f"models-{self.name}/my-model-{self.ep}-{ext}.{type}"
      




