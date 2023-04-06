import rclpy

from rclpy.node import Node
from memory_profiler import profile
import sys
import gc
import numpy as np
#from tensorflow.keras.callbacks import Callback
#from tensorflow.keras import backend as k

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

class ModifiedTensorBoard(TensorBoard):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.step = 1
        self.writer = tf.summary.create_file_writer(self.log_dir)
        self._log_write_dir = self.log_dir

    def set_model(self, model):
        self.model = model

        self._train_dir = os.path.join(self._log_write_dir, 'train')
        self._train_step = self.model._train_counter

        self._val_dir = os.path.join(self._log_write_dir, 'validation')
        self._val_step = self.model._test_counter

        self._should_write_train_graph = False

    def on_epoch_end(self, epoch, logs=None):
        self.update_stats(**logs)

    def on_batch_end(self, batch, logs=None):
        pass

    def on_train_end(self, _):
        pass

    def update_stats(self, **stats):
        with self.writer.as_default():
            for key, value in stats.items():
                tf.summary.scalar(key, value, step=self.step)
                self.writer.flush()


MODEL_NAME = '2x256'


class Dqn(Node):

    def __init__(self):
        super().__init__('dqn')
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        #self.ep =255
        self.ep =200
        self.test=False
        self.agents = [ACNetwork("robot-1",True, self.ep),
                       ACNetwork("robot-2",True, self.ep),
                        ACNetwork("robot-3",True, self.ep),
                        ACNetwork("robot-4",True, self.ep)
                       ]
        self.num_agents=4
   
        self.actions = [-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2]
        self.actions_size = 5
        self.minbatch_size = 64
        self.episode_length = 10_000
        self.steps_per_episode = 700
        
        self.episode_size = 3000

        self.train_every=1

        #self.epsilon = 1
        #self.EPSILON_DECAY = 0.992
        self.EPSILON_DECAY = 0.995
        self.MIN_EPSILON = 0.2
        self.MIN_REPLAY_MEMORY_SIZE = 500
        self.env_result_client = self.create_client(Mac, "env_result")
        self.reset_sim_client = self.create_client(Empty, "reset_sim")
        self.stop = True
        self.save_every=10
        #std_dev = 0.2
        
 
        self.tau=0.001
        self.rewards = [0 for _ in range(len(self.agents))]
        self.dones = [False for _ in range(self.num_agents)]

        self.current_states = [0.0 for _ in range(self.num_agents)]
        self.next_states = [0.0 for _ in range(self.num_agents)]
    
        self.std_dev=0.15
        self.ou_noise = OUActionNoise(mean=np.zeros(1), std_deviation=float(self.std_dev) * np.ones(1))
        # self.tensorboard = ModifiedTensorBoard(
        #     log_dir="logs/{}-{}".format(MODEL_NAME, int(time.time())))

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
                        ).states[i*4:i*4+4]
                        
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

                actions = [0 for _ in range(self.num_agents)]
                

                for index,agent in enumerate(self.agents):
                    if (not self.test):

                        noise = self.ou_noise()
                    else:
                        noise=0
                    state = tf.expand_dims(tf.convert_to_tensor(self.current_states[index]), 0)
                  
                    actions[index] = float(agent.policy(state, noise)[0])
                    
                
                  

                
                self.req.actions = actions

                future = self.env_result_client.call_async(self.req)
                #rclpy.spin_until_future_complete(self, future)
                
                while rclpy.ok():
            
                    rclpy.spin_once(self)
                    if future.done():
                        if future.result() is not None:
                            # Next state and reward
                            for i in range(self.num_agents):
                                
                                self.next_states[i] = future.result(
                                ).states[i*4:i*4+4]
                                self.rewards[i] = future.result().rewards[i]
                                self.returns[i] += self.rewards[i]
                                self.dones[i] = future.result().dones[i]
                               
                        else:
                            self.get_logger().error(
                                'Exception while calling service: {0}'.format(future.exception()))
                        break

                for index,agent in enumerate(self.agents):
                
                        if (not self.test and not self.dones[index]):
                       
                            agent.update_replay_buffer(
                                (self.current_states[index], self.rewards[index], actions[index], self.next_states[index], self.dones[index]))
                            #if(self.ep%self.train_every==0):
                               # print("training ep",self.ep)
                            agent.learn()
                            agent.update_target(agent.target_actor.variables,agent.actor_model.variables, self.tau)
                            agent.update_target(agent.target_critic.variables,agent.critic_model.variables, self.tau)
                       
                        self.current_states[index] = self.next_states[index]
                       

                       
                        

                    # if (done):

                    #     req = Empty.Request()
                    #     while not self.reset_sim_client.wait_for_service(timeout_sec=1.0):
                    #         self.get_logger().info('service not available, waiting again...')

                    #     self.reset_sim_client.call_async(req)
                    #     time.sleep(0.5)
                    #     # done=False
                    #     break

                        time.sleep(0.01)
               
                # if (i == self.steps_per_episode  and not self.test):
                   
                #     done = True
                #     req = Empty.Request()
                #     while not self.reset_sim_client.wait_for_service(timeout_sec=1.0):
                #         self.get_logger().info('service not available, waiting again...')

                #     self.reset_sim_client.call_async(req)
                #     time.sleep(0.5)
                # i += 1

            
            for index, agent in enumerate(self.agents):
                print(f"robot -{index+1} rewards", self.returns[index])
                with summary_writer.as_default():
                    tf.summary.scalar(f'rewards{index+1}', self.returns[index], step=self.ep)
                if (self.ep % self.save_every == 0 and self.ep!=0) and not self.test:
                    
                    agent.save_data(self.ep,self.rewards[index])
            if(self.ep%40==0 and self.ep!=0 and self.std_dev>0.01):
               self.std_dev-=0.01
               self.ou_noise = OUActionNoise(mean=np.zeros(1), std_deviation=float(self.std_dev) * np.ones(1))       
            
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
