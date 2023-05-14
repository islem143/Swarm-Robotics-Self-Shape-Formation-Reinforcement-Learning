from tensorflow import keras
import tensorflow as tf


import numpy as np



from copy import copy
from .agent import Agent

from .replay_buffer import ReplayBuffer

physical_devices = tf.config.list_physical_devices('GPU')
try:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
except:
    # Invalid device or cannot modify virtual devices once initialized.
    pass
summary_writer = tf.summary.create_file_writer('logs')

critic_loss = keras.losses.MeanSquaredError()


def loss_actor(y):
    return -tf.math.reduce_mean(y)


custom_objects = {"custom_loss_actor": loss_actor}
keras.utils.get_custom_objects().update(custom_objects)


class SuperAgent():
    def __init__(self, num_agents=2,state_size=24,action_size=2, ep=0) -> None:
        self.num_agents = num_agents
        self.action_size=action_size
        self.state_size=state_size
        self.ep = ep
        self.agents = [Agent(f"robot-{index+1}",False,0,self.state_size,self.action_size,self.num_agents) for index in range(self.num_agents)]
        self.replay_buffer = ReplayBuffer(
            num_agents=self.num_agents, state_size=self.state_size, action_size=self.action_size)
        #self.std_dev = 0.35
        self.tau = 0.001
        self.discout_factor = 0.99
        self.batch_size = 128
        self.noise2 = 0.0
        self.MIN_REPLAY_MEMORY_SIZE = 5000
    def set_episode(self, ep):
        self.ep = ep

    def set_noise(self, noise):
        self.noise = noise

    def set_noise2(self, noise):
        self.noise2 = noise

    def get_actions(self, state):
        
        res = [self.agents[index].policy(state[index], self.noise(), np.abs(
            self.noise2())) for index in range(self.num_agents)]
       
        a = []
        for r in res:
            a.append(float(r[0]))
            a.append(float(r[1]))
       
        return a
    @tf.function
    def update_target(self,target_weights, weights, tau):
  
     for (a, b) in zip(target_weights, weights):
        a.assign(b * tau + a * (1 - tau))

    #@tf.function
    def update(self, states, next_states, rewards, dones, actions,done_counter):
        
        
        for i in range(self.num_agents):
         if (done_counter[i] <= 1):
           
            with tf.GradientTape() as tape:
                #concat_actions = tf.concat(actions, axis=1)
                
                target_actions = [tf.concat(self.agents[index].target_actor(
                    next_states[:,i*self.state_size:i*self.state_size+self.state_size], training=True), axis=1) for index in range(self.num_agents)]
                concat_target_actions = tf.concat(target_actions, axis=1)
               
                print()
                y = tf.reshape(rewards[:, i], (-1, 1)) + self.discout_factor * self.agents[i].target_critic(
                    [next_states, concat_target_actions], training=True
                )*(1-tf.reshape(dones[:, i], (-1, 1)))
               
                
                critic_value = self.agents[i].critic_model(
                    [states, actions], training=True)
            
                c_loss = critic_loss(y, critic_value)
               

            critic_grad = tape.gradient(
                c_loss, self.agents[i].critic_model.trainable_variables)
            
            self.agents[i].critic_optimizer.apply_gradients(
                zip(critic_grad, self.agents[i].critic_model.trainable_variables))
            with summary_writer.as_default():
                tf.summary.scalar(
                    f'loss_critic-{self.agents[i].name}', c_loss, step=self.agents[i].critic_optimizer.iterations)
        
            with tf.GradientTape() as tape:
                policy_actions = [tf.concat(self.agents[index].actor_model(
                    states[:,i*self.state_size:i*self.state_size+self.state_size], training=True), axis=1) for index in range(self.num_agents)]
                concat_policy_actions = tf.concat(policy_actions, axis=1)
               
             
                

      
         
                critic_val = self.agents[i].critic_model(
                    [states, concat_policy_actions], training=True)
            
                actor_loss = loss_actor(critic_val)
               
                

            actor_grad = tape.gradient(
                actor_loss, self.agents[i].actor_model.trainable_variables)
     
           
            self.agents[i].actor_optimizer.apply_gradients(
                zip(actor_grad, self.agents[i].actor_model.trainable_variables)
            )
            with summary_writer.as_default():
                tf.summary.scalar(
                    f'loss_actor-{self.agents[i].name}', actor_loss, step=self.agents[i].actor_optimizer.iterations)
        # with tf.GradientTape(persistent=True) as tape:

        #     target_actions = [tf.concat(self.agents[index].target_actor(
        #         actor_next_states[index], training=True),axis=1) for index in range(self.num_agents) ]
        #     policy_actions=[tf.concat(self.agents[index].actor_model(actor_states[index],training=True),axis=1) for index in range(self.num_agents) ]

        #     concat_actions=tf.concat(actor_actions,axis=1)

        #     concat_target_actions=tf.concat(target_actions,axis=1)

        #     concat_policy_actions=tf.concat(policy_actions,axis=1)

        #     target_critics = [self.agents[index].target_critic(
        #         [next_states, concat_target_actions], training=True) for index in range(self.num_agents) if done_counter[index]<=1 ]
        #     critic_values_actor=[self.agents[index].critic_model(
        #         [states,concat_policy_actions], training=True) for index in range(self.num_agents) if done_counter[index]<=1  ]

        #     critic_values=[self.agents[index].critic_model(
        #         [states, concat_actions], training=True) for index in range(self.num_agents) if done_counter[index]<=1  ]

        #     y=[tf.reshape(rewards[:, index],(-1,1)) +self.discout_factor*target_critics[index]*(1-tf.reshape(dones[:,index],(-1,1))) for index in range(self.num_agents) if done_counter[index]<=1  ]

        #     critic_losses=[critic_loss(y[index],critic_values[index]) for index in range(self.num_agents) if done_counter[index]<=1  ]

        #     actor_losses=[loss_actor(critic_values_actor[index]) for index in range(self.num_agents) if done_counter[index]<=1  ]

        # critic_grads=[tape.gradient(critic_losses[index],self.agents[index].critic_model.trainable_variables) for index in range(self.num_agents) if done_counter[index]<=1  ]
        # actor_grads=[tape.gradient(actor_losses[index],self.agents[index].actor_model.trainable_variables)  for index in range(self.num_agents) if done_counter[index]<=1  ]

        # for index in range(self.num_agents):
        #      if(done_counter[index]<=1):
        #         self.agents[index].critic_optimizer.apply_gradients(zip(critic_grads[index],self.agents[index].critic_model.trainable_variables))
        #         self.agents[index].actor_optimizer.apply_gradients(zip(actor_grads[index],self.agents[index].actor_model.trainable_variables))
        #         with summary_writer.as_default():
        #             tf.summary.scalar(f'loss_critic-{self.agents[index].name}', critic_losses[index], step=self.agents[index].critic_optimizer.iterations)
        #             tf.summary.scalar(f'loss_actor-{self.agents[index].name}', actor_losses[index], step=self.agents[index].actor_optimizer.iterations)
   
    def train(self, done_counter):

        if (self.MIN_REPLAY_MEMORY_SIZE > self.replay_buffer.buffer_counter):
            return
        states, next_states, rewards, dones,actions = self.replay_buffer.get_minibatch(
            self.batch_size)

        self.update(states, next_states, rewards, dones,actions,list(done_counter.values()))
        for index, agent in enumerate(self.agents):
            if (done_counter[index] <= 1):
    
                self.update_target(
                    agent.target_actor.variables, agent.actor_model.variables, self.tau)
                self.update_target(
                    agent.target_critic.variables, agent.critic_model.variables, self.tau)
