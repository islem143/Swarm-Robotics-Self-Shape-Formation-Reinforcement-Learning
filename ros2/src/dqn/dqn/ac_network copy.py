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
summary_writer = tf.summary.create_file_writer('logs')

loss_function = keras.losses.MeanSquaredError()

def loss_actor(y):
    return -tf.math.reduce_mean(y)
custom_objects = {"custom_loss_actor": loss_actor}
keras.utils.get_custom_objects().update(custom_objects)
class ACNetwork():
    def __init__(self, name, model_load=False, ep=0,load_buffer=True) -> None:
        self.name = name
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.upper_bound=np.pi
        self.lower_bound=-np.pi
        self.load_buffer=load_buffer
        # self.critic_lr = 0.001

        # self.actor_lr = 0.0001
        self.critic_lr = 0.001
        self.actor_lr = 0.0001
        self.critic_optimizer = tf.keras.optimizers.Adam(learning_rate=self.critic_lr)
        self.actor_optimizer = tf.keras.optimizers.Adam(learning_rate=self.actor_lr)
        self.buffer_counter=0
        self.buffer_capacity=150_000
        self.state_size =6
        self.state_buffer = np.zeros((self.buffer_capacity, 56))
        self.action_buffer = np.zeros((self.buffer_capacity,2))
        self.reward_buffer = np.zeros((self.buffer_capacity, 1))
        self.next_state_buffer = np.zeros((self.buffer_capacity,56))
        self.dones = np.zeros((self.buffer_capacity,1))
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
            
            # Instead of list of tuples as the exp.replay concept go
            # We use different np.arrays for each tuple element
            self.state_buffer = np.zeros((self.buffer_capacity, 56))
            self.action_buffer = np.zeros((self.buffer_capacity,2))
            self.reward_buffer = np.zeros((self.buffer_capacity, 1))
            self.next_state_buffer = np.zeros((self.buffer_capacity,56))
            self.dones = np.zeros((self.buffer_capacity,1))
            self.ep = ep
            
        ep_rewards=[]  
       
        #learning_rate=0.00025
        
        # to note we are having the same target of if we load the model
      
      

        
        self.discout_factor = 0.99
        self.minbatch_size = 256
        self.MIN_REPLAY_MEMORY_SIZE =5000
      

       

        self.target_update_counter = 0

    def create_actor_model(self):
    
        init1 = tf.random_uniform_initializer(minval=-0.003, maxval=0.003)
        init2 = tf.random_uniform_initializer(minval=-0.0003, maxval=0.0003)

        inputs = keras.layers.Input(shape=(56,))
        out = keras.layers.Dense(400, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(inputs)
        out = keras.layers.BatchNormalization()(out)
        out=keras.layers.Dropout(0.2)(out)
        out = keras.layers.Dense(300, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(out)
        # out = keras.layers.BatchNormalization()(out)
        # out = keras.layers.Dense(128, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(out)
        
        # out = keras.layers.BatchNormalization()(out)
        # out = keras.layers.Dense(128, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(out)
  
        out = keras.layers.BatchNormalization()(out)
        out=keras.layers.Dropout(0.2)(out)
     
        outputs = keras.layers.Dense(1, activation="tanh",kernel_initializer=init1)(out)
    
        outputs2 = keras.layers.Dense(1, activation="tanh",kernel_initializer=init2)(out)
    


        
        outputs = outputs * self.upper_bound
        outputs2=(outputs2+1)*0.125+0.25
        model = tf.keras.Model(inputs, [outputs,outputs2])
        return model
    
    def create_critic_model(self):
        state_input = keras.layers.Input(shape=(56))
        state_out = keras.layers.Dense(512, activation="relu",
                                       kernel_initializer=keras.initializers.GlorotNormal())(state_input)
       
        action_input = keras.layers.Input(shape=(2))
        action_out = keras.layers.Dense(128, activation="relu",
                                        kernel_initializer=keras.initializers.GlorotNormal())(action_input)
     
        concat = keras.layers.Concatenate()([state_out, action_out])

        out = keras.layers.Dense(256, kernel_regularizer=keras.regularizers.l2(0.01),
                                 activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(concat)
        out=keras.layers.Dropout(0.2)(out)
     
        out = keras.layers.Dense(256, activation="relu",kernel_regularizer=keras.regularizers.l2(0.01),
                                 kernel_initializer=keras.initializers.GlorotNormal())(out)
        out=keras.layers.Dropout(0.2)(out)
       
        outputs = keras.layers.Dense(1)(out)
    
        model = tf.keras.Model([state_input, action_input], outputs)

        return model

    def policy(self,state, noise,noise2):
        #state=tf.expand_dims(tf.convert_to_tensor(state), 0)
        sampled_actions = tf.squeeze(self.actor_model(state))
        angular=sampled_actions[0]
        velocity=sampled_actions[1]
        #print("samlple",sampled_actions)
        
       
        # Adding noise to action
        angular = angular.numpy() + noise
        velocity=velocity.numpy() + noise2
        # We make sure action is within bounds
        angular = np.clip(angular, self.lower_bound, self.upper_bound)
        velocity = np.clip(velocity, 0.25, 0.5)
        #print(legal_action)

        return [np.squeeze(angular),np.squeeze(velocity)]
    
   

    @tf.function
    def update(
        self, state_batch, action_batch, reward_batch, next_state_batch,dones
    ):
            
            with tf.GradientTape() as tape:
                target_actions = self.target_actor(next_state_batch, training=True)
                target_actions=tf.concat(target_actions,axis=1)
            
                y = reward_batch + self.discout_factor * self.target_critic(
                    [next_state_batch, target_actions], training=True
                )*(1-dones)
                
            
                critic_value = self.critic_model([state_batch, action_batch], training=True)
          
                critic_loss = loss_function(y,critic_value)
                
                
               
            critic_grad = tape.gradient(critic_loss, self.critic_model.trainable_variables)
            self.critic_optimizer.apply_gradients(
                zip(critic_grad, self.critic_model.trainable_variables)
            )
            with summary_writer.as_default():
              tf.summary.scalar(f'loss_critic-{self.name}', critic_loss, step=self.critic_optimizer.iterations)

            with tf.GradientTape() as tape:
                actions = self.actor_model(state_batch, training=True)
                actions=tf.concat(actions,axis=1)
                critic_value = self.critic_model([state_batch, actions], training=True)
               
    
                actor_loss = loss_actor(critic_value)
           

            actor_grad = tape.gradient(actor_loss, self.actor_model.trainable_variables)
            self.actor_optimizer.apply_gradients(
                zip(actor_grad, self.actor_model.trainable_variables)
            )
            with summary_writer.as_default():
              tf.summary.scalar(f'loss_actor-{self.name}', actor_loss, step=self.actor_optimizer.iterations)

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
        
    
     
        record_range = min(self.buffer_counter, self.buffer_capacity)
        # Randomly sample indices
        batch_indices = np.random.choice(record_range, self.minbatch_size)
        #batch_indices = np.linspace(0, record_range-1, num=self.minbatch_size, dtype=int)
        
        # Convert to tensors
        state_batch = tf.convert_to_tensor(self.state_buffer[batch_indices])
        action_batch = tf.convert_to_tensor(self.action_buffer[batch_indices])
     
        reward_batch = tf.convert_to_tensor(self.reward_buffer[batch_indices])
        reward_batch = tf.cast(reward_batch, dtype=tf.float32)
        next_state_batch = tf.convert_to_tensor(self.next_state_buffer[batch_indices])
        dones = tf.convert_to_tensor(self.dones[batch_indices])
        dones = tf.cast(dones, dtype=tf.float32)
        
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

        if(self.load_buffer):
            path = os.path.join(self.dir_path, self.get_model_file_name("json"))
            self.buffer_counter=Utils.load_json(path, "counter")
        
            
        
            path = os.path.join(self.dir_path, self.get_model_file_name("obj","state"))
            self.state_buffer= Utils.load_pickle(path)
            
            
            path = os.path.join(self.dir_path, self.get_model_file_name("obj","reward"))
            self.reward_buffer= Utils.load_pickle(path)
            path = os.path.join(self.dir_path, self.get_model_file_name("obj","action"))
            self.action_buffer= Utils.load_pickle(path)
            path = os.path.join(self.dir_path, self.get_model_file_name("obj","next"))
            self.next_state_buffer= Utils.load_pickle(path)
            path = os.path.join(self.dir_path, self.get_model_file_name("obj","done"))
            self.dones= Utils.load_pickle(path)
       

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
        actor.compile(optimizer=self.actor_optimizer, loss="custom_loss_actor")
        target_actor.compile(optimizer=self.actor_optimizer, loss="custom_loss_actor")
        critic.compile(optimizer=self.critic_optimizer, loss=loss_function)
        target_critic.compile(optimizer=self.critic_optimizer, loss=loss_function)
        Utils.save_model(actor, path1)
        Utils.save_model(target_actor, path2)
        Utils.save_model(critic, path3)
        Utils.save_model(target_critic, path4)
        path = os.path.join(self.dir_path, self.get_model_file_name("json"))
        data = {"reward":reward,"counter":self.buffer_counter}
        Utils.save_json(path, data)
       
        path = os.path.join(self.dir_path, self.get_model_file_name("obj","state"))
        Utils.save_pickle(path, self.state_buffer)
        path = os.path.join(self.dir_path, self.get_model_file_name("obj","reward"))
        Utils.save_pickle(path, self.reward_buffer)
        path = os.path.join(self.dir_path, self.get_model_file_name("obj","action"))
        Utils.save_pickle(path, self.action_buffer)
        path = os.path.join(self.dir_path, self.get_model_file_name("obj","next"))
        Utils.save_pickle(path, self.next_state_buffer)
        path = os.path.join(self.dir_path, self.get_model_file_name("obj","done"))
        Utils.save_pickle(path, self.dones)

    def get_model_file_name(self, type,ext=None):
        return f"models-{self.name}/my-model-{self.ep}-{ext}.{type}"
      