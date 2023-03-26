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
from .dqn_network import Network

AGGREGATE_STATS_EVERY = 5

# class ClearMemory(Callback):
#     def on_epoch_end(self, epoch, logs=None):
#         gc.collect()
#         k.clear_session()


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
        self.ep =200
        self.test=True
        self.agents = [Network("robot-1",True, self.ep),
                     ]
        self.epsilon = self.agents[0].get_epsilon()

        self.actions = [-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2]
        self.actions_size = 5
        self.minbatch_size = 64
        self.episode_length = 10_000
        self.steps_per_episode = 700
        self.rewards = [0 for _ in range(len(self.agents))]
        self.episode_size = 3000

        self.current_states = [0, 0]
        #self.epsilon = 1
        #self.EPSILON_DECAY = 0.992
        self.EPSILON_DECAY = 0.99
        self.MIN_EPSILON = 0.1
        self.MIN_REPLAY_MEMORY_SIZE = 1000
        self.env_result_client = self.create_client(Dqnn, "env_result")
        self.reset_sim_client = self.create_client(Empty, "reset_sim")
        self.stop = False
        # self.tensorboard = ModifiedTensorBoard(
        #     log_dir="logs/{}-{}".format(MODEL_NAME, int(time.time())))

        self.start()
    def get_init_state(self):
     for index, agent in enumerate(self.agents):
        self.req = Dqnn.Request()
        self.req.init = True
        self.req.id = 250+index
       
        future = self.env_result_client.call_async(self.req)
        while rclpy.ok():
            rclpy.spin_once(self)
            if future.done():
                    if future.result() is not None:
                                # Next state and reward
                        self.current_states[index] = future.result().state

                    else:
                        self.get_logger().error(
                            'Exception while calling service: {0}'.format(future.exception()))
                    break 
    def start(self):

        for _ in range(self.episode_length):
            time.sleep(1)
            if (psutil.virtual_memory().percent > 92):
                self.stop = True
                print("finished")
                sys.exit()

                break
            self.get_init_state()
            self.ep += 1
            print("ep=", self.ep)
            self.rewards = [0 for _ in range(len(self.agents))]
            done=False

            while not done:

                # while not self.env_result_client.wait_for_service(timeout_sec=1.0):
                #     self.get_logger().info('service not available, waiting again...')

                for index, agent in enumerate(self.agents):
                    reward = 0
                    self.req = Dqnn.Request()
                    self.req.init = False
                    self.req.id = index+1
                  
                    if (not self.test):
                        if np.random.random() > self.epsilon:
                            action = np.argmax(
                                agent.get_action(self.current_states[index]))
                            print(action)
                            
                            

                        else:

                            action = np.random.randint(0, self.actions_size)
                           
                            
                    else:
                        action = np.argmax(
                            agent.get_action(self.current_states[index]))
                    
                   
                  
                            

                    self.req.action = float(action)
                    

                    future = self.env_result_client.call_async(self.req)
                    #rclpy.spin_until_future_complete(self, future)
                    while rclpy.ok():

                        rclpy.spin_once(self)
                        if future.done():
                            if future.result() is not None:
                                # Next state and reward
                                next_state = future.result().state
                                reward = future.result().reward

                                done = future.result().done

                            else:
                                self.get_logger().error(
                                    'Exception while calling service: {0}'.format(future.exception()))
                            break
                    if (not self.test):

                        self.rewards[index] += reward
                        agent.update_replay_buffer(
                            (self.current_states[index], reward, action, next_state, done))
                    self.current_states[index] = next_state
                    if (not self.test):
                        agent.train(done)

                    

                    time.sleep(0.01)

                
                

            if (self.epsilon > self.MIN_EPSILON) and not self.test:
                self.epsilon *= self.EPSILON_DECAY
                self.epsilon = max(self.MIN_EPSILON, self.epsilon)
                 
            for index, agent in enumerate(self.agents):
                print(f"robot -{index+1} rewards", self.rewards[index])
                if (self.ep % 10 == 0 and self.ep!=0) and not self.test:
                    agent.save_data(self.ep, self.epsilon, self.rewards[index])
                   

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
