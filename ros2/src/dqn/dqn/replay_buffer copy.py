import numpy as np
import tensorflow as tf
class ReplayBuffer():
    

    def __init__(self,state_size=4,num_agents=2,action_size=1) -> None:
        self.buffer_capacity=100_000
        self.state_size=state_size
        self.num_agents=num_agents
        self.action_size=action_size
        self.states=np.zeros((self.buffer_capacity,self.state_size*num_agents))
        self.next_states=np.zeros((self.buffer_capacity,self.state_size*num_agents))
       # self.actions=np.zeros((self.buffer_capacity,self.action_size*num_agents))
        self.rewards=np.zeros((self.buffer_capacity,self.num_agents))
        self.dones=np.zeros((self.buffer_capacity,self.num_agents))
        self.actor_states=np.zeros((self.num_agents,self.buffer_capacity,self.state_size))
        self.actor_next_states=np.zeros((self.num_agents,self.buffer_capacity,self.state_size))
        self.actor_actions=np.zeros((self.num_agents,self.buffer_capacity,self.action_size))
        self.buffer_counter=0
        

    
    def add_record(self, states,next_states,rewards,dones,actor_states,actor_next_states,actor_actions):
        
   
        self.buffer_counter+=1
    
            
        index = self.buffer_counter % self.buffer_capacity
        self.states[index]=states 
        self.next_states[index]=next_states
        #self.actions[index]=actions
        self.rewards[index]=rewards
        self.dones[index]=dones
      
     

        for i in range(self.num_agents):
            
            self.actor_states[i][index]=actor_states[i]
            self.actor_next_states[i][index]=actor_next_states[i]
            self.actor_actions[i][index]=np.array(actor_actions[i*2:i*2+2])
        
     
      

        
        
    def get_minibatch(self,batch_size):
        record_range = min(self.buffer_counter, self.buffer_capacity)
        # Randomly sample indices
        batch_indices = np.random.choice(record_range, batch_size)
        
        # Convert to tensors
        states_batch = tf.convert_to_tensor(self.states[batch_indices])
       # actions_batch = tf.convert_to_tensor(self.actions[batch_indices])
        next_states_batch = tf.convert_to_tensor(self.next_states[batch_indices])
        rewards_batch = tf.convert_to_tensor(self.rewards[batch_indices])
        rewards_batch = tf.cast(rewards_batch, dtype=tf.float32)
        dones = tf.convert_to_tensor(self.dones[batch_indices])
        dones = tf.cast(dones, dtype=tf.float32)
        actors_state_batch=[ tf.convert_to_tensor(self.actor_states[index][batch_indices]) for index in range(self.num_agents)]
        actors_next_state_batch=[tf.convert_to_tensor(self.actor_next_states[index][batch_indices]) for index in range(self.num_agents)]
        actors_actions_batch=[tf.convert_to_tensor(self.actor_actions[index][batch_indices]) for index in range(self.num_agents)]
        
        return states_batch,next_states_batch,rewards_batch,dones,actors_state_batch,actors_next_state_batch,actors_actions_batch
