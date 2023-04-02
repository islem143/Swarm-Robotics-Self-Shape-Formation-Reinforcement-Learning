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
# physical_devices = tf.config.list_physical_devices('GPU')
# try:
#     tf.config.experimental.set_memory_growth(physical_devices[0], True)
# except:
#     # Invalid device or cannot modify virtual devices once initialized.
#     pass
summary_writer = tf.summary.create_file_writer('logs')

loss_function = keras.losses.MeanSquaredError()

def loss_actor(y):
    return -tf.math.reduce_mean(y)
custom_objects = {"custom_loss_actor": loss_actor}
keras.utils.get_custom_objects().update(custom_objects)

class Agent():
    def __init__(self, name,model_load=False, ep=0,test=False,num_agents=2,state_size=4,action_size=1) -> None:
        self.name = name
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.upper_bound=np.pi/2
        self.lower_bound=-np.pi/2
        # self.critic_lr = 0.001
        self.num_agents=num_agents
        self.state_size=state_size
        self.action_size=action_size
        self.test=test
        # self.actor_lr = 0.0001
        self.critic_lr = 0.001
        self.actor_lr = 0.0001
        self.critic_optimizer = tf.keras.optimizers.Adam(learning_rate=self.critic_lr)
        self.actor_optimizer = tf.keras.optimizers.Adam(learning_rate=self.actor_lr)
        self.buffer_counter=0
        self.buffer_capacity=100_000
        self.state_buffer = np.zeros((self.buffer_capacity, 4))
        self.action_buffer = np.zeros((self.buffer_capacity,1))
        self.reward_buffer = np.zeros((self.buffer_capacity, 1))
        self.next_state_buffer = np.zeros((self.buffer_capacity,4))
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
            self.state_buffer = np.zeros((self.buffer_capacity, 4))
            self.action_buffer = np.zeros((self.buffer_capacity,1))
            self.reward_buffer = np.zeros((self.buffer_capacity, 1))
            self.next_state_buffer = np.zeros((self.buffer_capacity,4))
            self.dones = np.zeros((self.buffer_capacity,1))
            self.ep = ep
            
        ep_rewards=[]  
       
        #learning_rate=0.00025
        
        # to note we are having the same target of if we load the model
      
      


        self.discout_factor = 0.99
        self.minbatch_size = 128
        self.MIN_REPLAY_MEMORY_SIZE =5000
      

       

        self.target_update_counter = 0

    def create_actor_model(self):
        # Initialize weights between -3e-3 and 3-e3
        last_init = tf.random_uniform_initializer(minval=-0.003, maxval=0.003)


        inputs = keras.layers.Input(shape=(self.state_size,))
        out = keras.layers.Dense(400, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(inputs)
        out=keras.layers.Dropout(0.5)(out)
        out = keras.layers.BatchNormalization()(out)
        out = keras.layers.Dense(300, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(out)
        out=keras.layers.Dropout(0.5)(out)
        out = keras.layers.BatchNormalization()(out)
     
        # out = keras.layers.Dense(128, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(out)
        # out=keras.layers.Dropout(0.2)(out)
        # out = keras.layers.BatchNormalization()(out)
        # out = keras.layers.Dense(512, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(out)
        # out=keras.layers.Dropout(0.2)(out)
        # out = keras.layers.BatchNormalization()(out)
        outputs = keras.layers.Dense(1, activation="tanh",kernel_initializer=last_init
   
)(out)

        
        outputs = outputs * self.upper_bound
        model = tf.keras.Model(inputs, outputs)
        return model
    
    def create_critic_model(self):
        state_input = keras.layers.Input(shape=(self.state_size*self.num_agents))
        state_out = keras.layers.Dense(300, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(state_input)
        #state_out = keras.layers.BatchNormalization()(state_out)
        # state_out = keras.layers.Dense(32, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(state_out)
        # state_out = keras.layers.BatchNormalization()(state_out)

            # Action as input
        action_input = keras.layers.Input(shape=(self.action_size*self.num_agents))
        action_out = keras.layers.Dense(300, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(action_input)
      #  action_out =  keras.layers.BatchNormalization()(action_out)
            # Both are passed through seperate layer before concatenating
        concat = keras.layers.Concatenate()([state_out, action_out])

        out = keras.layers.Dense(400, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(concat)
        out=keras.layers.Dropout(0.5)(out)
       # out = keras.layers.BatchNormalization()(out)
        out = keras.layers.Dense(300, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(out)
        out=keras.layers.Dropout(0.5)(out)
       # out = keras.layers.BatchNormalization()(out)
        # = keras.layers.Dense(512, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(out)
        #out=keras.layers.Dropout(0.3)(out)
       # out = keras.layers.BatchNormalization()(out)
        # out = keras.layers.Dense(512, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(out)
        # out=keras.layers.Dropout(0.2)(out)
        # out = keras.layers.BatchNormalization()(out)
        outputs = keras.layers.Dense(1)(out)

        # Outputs single value for give state-action
        model = tf.keras.Model([state_input, action_input], outputs)

        return model

    def policy(self,state, noise):
       
        state = tf.expand_dims(tf.convert_to_tensor(state), 0)
        sampled_actions = tf.squeeze(self.actor_model(state))
        #print("samlple",sampled_actions)
        
       
        # Adding noise to action
        sampled_actions = sampled_actions.numpy() + noise
         
        # We make sure action is within bounds
        legal_action = np.clip(sampled_actions, self.lower_bound, self.upper_bound)
        #print(legal_action)

        return [np.squeeze(legal_action)][0]
    
   

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
               
                critic_value = self.critic_model([state_batch, actions], training=True)
                # Used `-value` as we want to maximize the value given
                # by the critic for our actions
                # q_mean = tf.math.reduce_mean(critic_value)
                # q_std = tf.math.reduce_std(critic_value)
                # q_normalized = (critic_value - q_mean) / q_std
                 
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

    

    
