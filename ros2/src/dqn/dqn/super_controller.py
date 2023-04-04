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




import time
from std_srvs.srv import Empty

from .ouNoise import OUActionNoise
from dqn_msg.srv import Mac
from .super_agent import SuperAgent
AGGREGATE_STATS_EVERY = 5

# class ClearMemory(Callback):
#     def on_epoch_end(self, epoch, logs=None):
#         gc.collect()
#         k.clear_session()

summary_writer = tf.summary.create_file_writer('logs')




def loss_actor(y):
    return -tf.math.reduce_mean(y)

critic_loss_function = keras.losses.MeanSquaredError()

custom_objects = {"custom_loss_actor": loss_actor}
class SuperController(Node):

    def __init__(self):
        super().__init__('dqn')
        self.state_size = 4
        self.action_size = 1
        self.num_agents =2
        self.test=False
        self.episode_length = 3000
        self.ep = 0
        self.super_agent = SuperAgent(num_agents=self.num_agents)
        self.current_actor_states = np.zeros(
            (self.num_agents, self.state_size), dtype=np.float32)
        self.next_actor_states = np.zeros(
            (self.num_agents, self.state_size), dtype=np.float32)
        self.actor_actions = np.zeros((self.num_agents,), dtype=np.float32)
        self.dones = np.zeros((self.num_agents,), dtype=np.float32)
        self.rewards = np.zeros((self.num_agents,), dtype=np.float32)
        self.states = np.zeros(
            (self.num_agents*self.state_size,), dtype=np.float32)

        self.next_states = np.zeros(
            (self.num_agents*self.state_size,), dtype=np.float32)
        self.actions = np.zeros(
            (self.num_agents*self.action_size,), dtype=np.float32)
        self.std_dev=0.5
        self.ou_noise = OUActionNoise(mean=np.zeros(1), std_deviation=float(self.std_dev) * np.ones(1))
        self.super_agent.set_noise(self.ou_noise)
        self.env_result_client = self.create_client(Mac, "env_result")
        self.reset_sim_client = self.create_client(Empty, "reset_sim")
        self.save_every=20
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
                        self.current_actor_states[i] = future.result(
                        ).states[i*self.state_size:i*self.state_size+self.state_size]

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
            self.super_agent.set_episode(self.ep)
            print("ep=", self.ep)
            self.rewards = [0.0 for _ in range(self.num_agents)]
            self.returns = [0.0 for _ in range(self.num_agents)]

            while not all(self.dones):

                self.req = Mac.Request()
                self.req.init = False
              
                self.actor_actions=self.super_agent.get_actions(self.current_actor_states)
                
               

                self.req.actions = self.actor_actions

                future = self.env_result_client.call_async(self.req)
                #rclpy.spin_until_future_complete(self, future)

                while rclpy.ok():

                    rclpy.spin_once(self)
                    if future.done():
                        if future.result() is not None:
                            # Next state and reward
                            for i in range(self.num_agents):

                                self.next_actor_states[i] = future.result(
                                ).states[i*4:i*4+4]
                                self.rewards[i] = future.result().rewards[i]
                                self.returns[i] += self.rewards[i]
                                self.dones[i] = future.result().dones[i]

                        else:
                            self.get_logger().error(
                                'Exception while calling service: {0}'.format(future.exception()))
                        break
               

                states=np.concatenate(self.current_actor_states)
                next_states=np.concatenate(self.next_actor_states)
               
                self.super_agent.replay_buffer.add_record(states,next_states,self.rewards,self.dones,self.current_actor_states,self.next_actor_states,self.actor_actions)
                self.current_actor_states=self.next_actor_states
              
                self.super_agent.train()
                

                    

                time.sleep(0.01)


            for index, agent in enumerate(self.super_agent.agents):
                print(f"robot -{index+1} rewards", self.returns[index])
                with summary_writer.as_default():
                    tf.summary.scalar(
                        f'rewards{index+1}', self.returns[index], step=self.ep)
               # if (self.ep % self.save_every == 0 and self.ep != 0) and not self.test:

                    #agent.save_data(self.ep, self.rewards[index])
            if (self.ep % 25 == 0 and self.ep != 0 and self.std_dev > 0.01):
                self.std_dev -= 0.01
                self.ou_noise = OUActionNoise(mean=np.zeros(
                    1), std_deviation=float(self.std_dev) * np.ones(1))
                self.super_agent.set_noise(self.ou_noise)
                

            print("self.std", self.std_dev)

            # if not self.ep % AGGREGATE_STATS_EVERY or self.ep == 1:
            #      average_reward = sum(
            #        ep_rewards[-AGGREGATE_STATS_EVERY:])/len(ep_rewards[-AGGREGATE_STATS_EVERY:])
            #      min_reward = min(ep_rewards[-AGGREGATE_STATS_EVERY:])
            #      max_reward = max(ep_rewards[-AGGREGATE_STATS_EVERY:])
            #      self.tensorboard.update_stats(
            #       reward_avg=average_reward, reward_min=min_reward, reward_max=max_reward, epsilon=self.epsilon)


def main(args=None):
    rclpy.init(args=args)

    dqn = SuperController()

    rclpy.spin(dqn)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    dqn.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
