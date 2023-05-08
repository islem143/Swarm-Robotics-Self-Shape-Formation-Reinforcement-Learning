import rclpy

from rclpy.node import Node
from memory_profiler import profile
import sys
import gc
import numpy as np


import tensorflow as tf





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







class SuperController(Node):

    def __init__(self):
        super().__init__('dqn')
        self.state_size = 24
        self.action_size = 2
        self.num_agents =1
        self.test=False
        self.episode_length = 3000
        self.ep = 0
        self.super_agent = SuperAgent(num_agents=self.num_agents,state_size=self.state_size,action_size=self.action_size)
        self.current_actor_states = np.zeros(
            (self.num_agents, self.state_size), dtype=np.float32)
        self.next_actor_states = np.zeros(
            (self.num_agents, self.state_size), dtype=np.float32)
        # to review
        self.actor_actions = np.zeros((self.num_agents*self.action_size), dtype=np.float32)
        self.dones = np.zeros((self.num_agents,), dtype=np.float32)
        self.rewards = np.zeros((self.num_agents,), dtype=np.float32)
        self.states = np.zeros(
            (self.num_agents*self.state_size,), dtype=np.float32)

        self.next_states = np.zeros(
            (self.num_agents*self.state_size,), dtype=np.float32)
      
        self.std_dev=0.20
        self.std_dev2=0.05
        self.done_counter={"0":0,"1":0,"2":0,"3":0}
        self.ou_noise2 = OUActionNoise(mean=np.zeros(1), std_deviation=float(self.std_dev2) * np.ones(1))
        self.ou_noise = OUActionNoise(mean=np.zeros(1), std_deviation=float(self.std_dev) * np.ones(1))
        self.super_agent.set_noise(self.ou_noise)
        self.super_agent.set_noise2(self.ou_noise2)
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
                                if(not self.dones[i]):    
                                    self.next_actor_states[i] = future.result(
                                    ).states[i*self.state_size:i*self.state_size+self.state_size]
                                    
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
               
                if (not self.test):
                  
                    states=np.concatenate(self.current_actor_states)
             
                    next_states=np.concatenate(self.next_actor_states)
                 
                    self.super_agent.replay_buffer.add_record(states,next_states,self.rewards,self.dones,self.current_actor_states,self.next_actor_states,self.actor_actions)
                    
                    self.super_agent.train(self.done_counter)
                self.current_actor_states=self.next_actor_states
                

                    

                time.sleep(0.01)


            for index, agent in enumerate(self.super_agent.agents):
                print(f"robot -{index+1} rewards", self.returns[index])
                if(not self.test and self.done_counter[index]<=1):
                    with summary_writer.as_default():
                     tf.summary.scalar(
                        f'rewards{index+1}', self.returns[index], step=self.ep)
                #if (self.ep % self.save_every == 0 and self.ep != 0) and not self.test:

                   # agent.save_data(self.ep, self.rewards[index])
           
                

       

  


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
