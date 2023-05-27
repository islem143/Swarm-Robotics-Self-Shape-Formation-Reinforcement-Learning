import rclpy

from rclpy.node import Node
from memory_profiler import profile
import sys
import gc
import numpy as np
#from tensorflow.keras.callbacks import Callback
#from tensorflow.keras import backend as k
from timeit import default_timer as timer   
import tensorflow as tf
from tensorflow import keras
from dqn_msg.srv import Dqnn
import psutil
from collections import deque
from .utils import Utils
import os
from keras.callbacks import TensorBoard
import random
import time
from std_srvs.srv import Empty
from .ac_network import ACNetwork
from .ouNoise import OUActionNoise
from dqn_msg.srv import Mac
AGGREGATE_STATS_EVERY = 5

# class ClearMemory(Callback):
#     def on_epoch_end(self, epoch, logs=None):
#         gc.collect()
#         k.clear_session()

summary_writer = tf.summary.create_file_writer('logs')




class Dqn(Node):

    def __init__(self):
        super().__init__('dqn')
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        #self.ep =255
        self.ep =1900
        self.test=True
        load_buffer=True
        load_model=True
        self.agents = [ACNetwork("robot-2",load_model, self.ep,load_buffer),  
                     
                       ACNetwork("robot-2",load_model, self.ep,load_buffer),
                       ACNetwork("robot-3",load_model, self.ep,load_buffer),
                       ACNetwork("robot-4",load_model, self.ep,load_buffer),
                       #ACNetwork("robot-2",load_model, self.ep,load_buffer),
                     # ACNetwork("robot-4",load_model, self.ep,load_buffer),
                   
                 
                      
                      
                       ]
        self.num_agents=4
   
        self.actions = [-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2]
        self.actions_size = 5
        self.minbatch_size = 64
        self.episode_length = 10_000
        self.steps_per_episode = 700
        
        self.episode_size = 3500

        self.train_every=1
        self.done_counter={"0":0,"1":0,'2':0,'3':0}



        #self.epsilon = 1
        #self.EPSILON_DECAY = 0.992
        self.EPSILON_DECAY = 0.995
        self.MIN_EPSILON = 0.2
        self.MIN_REPLAY_MEMORY_SIZE = 3000
        self.env_result_client = self.create_client(Mac, "env_result")
        self.reset_sim_client = self.create_client(Empty, "reset_sim")
        self.stop = True
        self.save_every=100
        #std_dev = 0.2
        
 
        self.tau=0.001
        self.rewards = [0 for _ in range(len(self.agents))]
        self.dones = [False for _ in range(self.num_agents)]

        self.current_states = [0.0 for _ in range(self.num_agents)]
        self.next_states = [0.0 for _ in range(self.num_agents)]
    
        self.std_dev=0.25
        self.std_dev2=0.08
        self.ou_noise = OUActionNoise(mean=np.zeros(1), std_deviation=float(self.std_dev) * np.ones(1))
        self.ou_noise2 = OUActionNoise(mean=np.zeros(1), std_deviation=float(self.std_dev2) * np.ones(1))
        
        self.start()

    def get_init_state(self):

        self.req = Mac.Request()
        self.req.init = True
        

        future = self.env_result_client.call_async(self.req)
        while rclpy.ok():
            rclpy.spin_once(self)
            if future.done():
                if future.result() is not None:
                    
                    for i in range(self.num_agents):
                        self.current_states[i] = future.result(
                        ).states[i*56:i*56+56]
                        
                else:
                    self.get_logger().error(
                        'Exception while calling service: {0}'.format(future.exception()))
                break
        
               
    def start(self):

        for _ in range(self.episode_length):
           
            
            time.sleep(1)

            self.dones = [False for _ in range(self.num_agents)]
            self.get_init_state()
            self.ep += 1
            print("ep=", self.ep)
            self.rewards = [0.0 for _ in range(len(self.agents))]
            self.returns = [0.0 for _ in range(len(self.agents))]
            
            while  not all(self.dones):
                
        
   
                self.req = Mac.Request()
                self.req.init = False

                actions = [0 for _ in range(self.num_agents*2)]
                

                for index,agent in enumerate(self.agents):
               
                    if (not self.test):

                        noise = self.ou_noise()
                        noise2 = self.ou_noise2()
                        
                    else:
                        noise=0
                        noise2=0
                        #noise = self.ou_noise()
                        #noise2 = np.abs(self.ou_noise2())
                    state = tf.expand_dims(tf.convert_to_tensor(self.current_states[index]), 0)
                    result=agent.policy(state, noise,noise2)
                    actions[index*2] =float(result[0])
                    actions[index*2+1]=float(result[1]) 
                
               
                 
                
                  

                
                self.req.actions = actions

                future = self.env_result_client.call_async(self.req)
                #rclpy.spin_until_future_complete(self, future)
                
                while rclpy.ok():
            
                    rclpy.spin_once(self)
                    if future.done():
                        if future.result() is not None:
                            # Next state and reward
                            for i in range(self.num_agents):
                                
                               
                                if(not self.dones[i]):
                                    self.next_states[i] = future.result(
                                    ).states[i*56:i*56+56]
                                    self.rewards[i] = future.result().rewards[i]
                                    self.returns[i] += self.rewards[i]

                                self.dones[i] = future.result().dones[i]
                                if(self.dones[i]):
                                    self.done_counter[i]+=1
                                else:
                                    self.done_counter[i]=0
                               
                        else:
                            self.get_logger().error(
                                'Exception while calling service: {0}'.format(future.exception()))
                        break

                for index,agent in enumerate(self.agents):
                
                        if (not self.test and   self.done_counter[index]<=1):
                            
                            agent.update_replay_buffer(
                                (self.current_states[index], self.rewards[index], actions[index*2:index*2+2], self.next_states[index], self.dones[index]))
                            #if(self.ep%self.train_every==0):
                               # print("training ep",self.ep)
                            agent.learn()
                            agent.update_target(agent.target_actor.variables,agent.actor_model.variables, self.tau)
                            agent.update_target(agent.target_critic.variables,agent.critic_model.variables, self.tau)
                       
                        self.current_states[index] = self.next_states[index]
                        time.sleep(0.005)   

                       
                        

                   
               
            

            
            for index, agent in enumerate(self.agents):
                print(f"robot -{index+1} rewards", self.returns[index])
                if(not self.test and self.done_counter[index]<=1):
                 with summary_writer.as_default():
                     tf.summary.scalar(f'rewards{index+1}', self.returns[index], step=self.ep)
                if (self.ep % self.save_every == 0 and self.ep!=0) and not self.test:
                    
                    agent.save_data(self.ep,self.rewards[index])
            #if(self.ep%40==0 and self.ep!=0 and self.std_dev>0.01):
               #self.std_dev-=0.01
              # self.ou_noise = OUActionNoise(mean=np.zeros(1), std_deviation=float(self.std_dev) * np.ones(1))       
            
            print("self.std",self.std_dev)       

            # if not self.ep % AGGREGATE_STATS_EVERY or self.ep == 1:
            #      average_reward = sum(
            #        ep_rewards[-AGGREGATE_STATS_EVERY:])/len(ep_rewards[-AGGREGATE_STATS_EVERY:])
            #      min_reward = min(ep_rewards[-AGGREGATE_STATS_EVERY:])
            #      max_reward = max(ep_rewards[-AGGREGATE_STATS_EVERY:])
            #      self.tensorboard.update_stats(
            #       reward_avg=average_reward, reward_min=min_reward, reward_max=max_reward, epsilon=self.epsilon)


def main(args=None):
    rclpy.init(args=args)

    dqn = Dqn()

    rclpy.spin(dqn)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    dqn.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()