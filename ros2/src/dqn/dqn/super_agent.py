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
from .agent import Agent
from rclpy.node import Node
from .replay_buffer import ReplayBuffer
from .ouNoise import OUActionNoise
# physical_devices = tf.config.list_physical_devices('GPU')
# try:
#     tf.config.experimental.set_memory_growth(physical_devices[0], True)
# except:
#     # Invalid device or cannot modify virtual devices once initialized.
#     pass
summary_writer = tf.summary.create_file_writer('logs')

critic_loss = keras.losses.MeanSquaredError()


def loss_actor(y):
    return -tf.math.reduce_mean(y)


custom_objects = {"custom_loss_actor": loss_actor}
keras.utils.get_custom_objects().update(custom_objects)


class SuperAgent():
    def __init__(self, num_agents=2,ep=0) -> None:
        self.num_agents = num_agents
        self.ep=ep 
        self.agents = [Agent(f"robot-{index+1}",num_agents=self.num_agents,model_load=False,) for index in range(self.num_agents)]
        self.replay_buffer = ReplayBuffer(num_agents=self.num_agents)
        #self.std_dev = 0.35
        self.tau = 0.001
        self.discout_factor = 0.99
        self.batch_size = 128
       
        self.MIN_REPLAY_MEMORY_SIZE =7000

    def set_episode(self,ep):
        self.ep=ep
    def set_noise(self,noise):
        self.noise=noise
    def get_actions(self, state):
        return [float(self.agents[index].policy(state[index], self.noise())) for index in range(self.num_agents)]
    

    @tf.function
    def update(self,states, next_states,rewards,dones,actor_states,actor_next_states,actor_actions):
        

        with tf.GradientTape(persistent=True) as tape:
           
            
            target_actions = [self.agents[index].target_actor(
                actor_next_states[index], training=True) for index in range(self.num_agents)]
            policy_actions=[self.agents[index].actor_model(actor_states[index],training=True) for index in range(self.num_agents)]
            concat_actions=tf.concat(actor_actions,axis=1)
            concat_target_actions=tf.concat(target_actions,axis=1)
           
            concat_policy_actions=tf.concat(policy_actions,axis=1)
          
            target_critics = [self.agents[index].target_critic(
                [next_states, concat_target_actions], training=True) for index in range(self.num_agents)]
            critic_values_actor=[self.agents[index].critic_model(
                [states,concat_policy_actions], training=True) for index in range(self.num_agents)]
          
            
           
          
            critic_values=[self.agents[index].critic_model(
                [states, concat_actions], training=True) for index in range(self.num_agents)]
            
            y=[tf.reshape(rewards[:, index],(-1,1)) +self.discout_factor*target_critics[index]*(1-tf.reshape(dones[:,index],(-1,1))) for index in range(self.num_agents)]
            
            critic_losses=[critic_loss(y[index],critic_values[index]) for index in range(self.num_agents)]
           
            actor_losses=[loss_actor(critic_values_actor[index]) for index in range(self.num_agents)]
            
              

            
        critic_grads=[tape.gradient(critic_losses[index],self.agents[index].critic_model.trainable_variables) for index in range(self.num_agents)]
        actor_grads=[tape.gradient(actor_losses[index],self.agents[index].actor_model.trainable_variables)  for index in range(self.num_agents)]


        for index in range(self.num_agents):
             self.agents[index].critic_optimizer.apply_gradients(zip(critic_grads[index],self.agents[index].critic_model.trainable_variables))
             self.agents[index].actor_optimizer.apply_gradients(zip(actor_grads[index],self.agents[index].actor_model.trainable_variables))
             with summary_writer.as_default():
                 tf.summary.scalar(f'loss_critic-{self.agents[index].name}', critic_losses[index], step=self.agents[index].critic_optimizer.iterations) 
                 tf.summary.scalar(f'loss_actor-{self.agents[index].name}', actor_losses[index], step=self.agents[index].actor_optimizer.iterations)
    
    def train(self):
        
        if (self.MIN_REPLAY_MEMORY_SIZE > self.replay_buffer.buffer_counter):
            return
        states, next_states, rewards, dones, actor_states, actor_next_states, actor_actions = self.replay_buffer.get_minibatch(
                self.batch_size)
        
        self.update(states, next_states, rewards, dones, actor_states, actor_next_states, actor_actions)
        for index,agent in enumerate(self.agents):
            agent.update_target(agent.target_actor.variables,agent.actor_model.variables, self.tau)
            agent.update_target(agent.target_critic.variables,agent.critic_model.variables, self.tau)