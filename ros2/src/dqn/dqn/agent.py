from tensorflow import keras
import tensorflow as tf


import numpy as np


import os


from rclpy.node import Node
# physical_devices = tf.config.list_physical_devices('GPU')
# try:
#     tf.config.experimental.set_memory_growth(physical_devices[0], True)
# except:
#     # Invalid device or cannot modify virtual devices once initialized.
#     pass




class Agent():
    def __init__(self, name, model_load=False, ep=0,state_size=24, action_size=2,
                             num_agents=1) -> None:
        self.name = name
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.upper_bound=np.pi
        self.lower_bound=-np.pi
        self.state_size=state_size
        self.action_size=action_size
        self.num_agents=num_agents
    
        self.critic_lr = 0.001
        self.actor_lr = 0.0001
        self.critic_optimizer = tf.keras.optimizers.Adam(learning_rate=self.critic_lr)
        self.actor_optimizer = tf.keras.optimizers.Adam(learning_rate=self.actor_lr)
      

       
        
        if (model_load):
            self.ep = ep
            self.load_data()
          
        else:
            
            self.actor_model = self.create_actor_model()
            self.critic_model = self.create_critic_model()

            self.target_actor = self.create_actor_model()
            self.target_critic = self.create_critic_model()

  
            
         
            
          
          
            self.ep = ep
       
      

       


   
    def create_actor_model(self):
    
        init1 = tf.random_uniform_initializer(minval=-0.003, maxval=0.003)
        init2 = tf.random_uniform_initializer(minval=-0.0003, maxval=0.0003)

        inputs = keras.layers.Input(shape=(18,))
        out = keras.layers.Dense(400, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(inputs)
        out = keras.layers.BatchNormalization()(out)
        out=keras.layers.Dropout(0.3)(out)
        out = keras.layers.Dense(300, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(out)
        # out = keras.layers.BatchNormalization()(out)
        # out = keras.layers.Dense(128, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(out)
        
        # out = keras.layers.BatchNormalization()(out)
        # out = keras.layers.Dense(128, activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(out)
  
        out = keras.layers.BatchNormalization()(out)
        out=keras.layers.Dropout(0.3)(out)
     
        outputs = keras.layers.Dense(1, activation="tanh",kernel_initializer=init1)(out)
    
        outputs2 = keras.layers.Dense(1, activation="tanh",kernel_initializer=init2)(out)
    


        
        outputs = outputs * self.upper_bound
        outputs2=(outputs2+1)*0.15+0.2
        model = tf.keras.Model(inputs, [outputs,outputs2])
        return model
    
    def create_critic_model(self):
        state_input = keras.layers.Input(shape=(18))
        state_out = keras.layers.Dense(512, activation="relu",
                                       kernel_initializer=keras.initializers.GlorotNormal())(state_input)
       
        action_input = keras.layers.Input(shape=(2))
        action_out = keras.layers.Dense(256, activation="relu",
                                        kernel_initializer=keras.initializers.GlorotNormal())(action_input)
     
        concat = keras.layers.Concatenate()([state_out, action_out])

        out = keras.layers.Dense(1024, kernel_regularizer=keras.regularizers.l2(0.01),
                                 activation="relu",kernel_initializer=keras.initializers.GlorotNormal())(concat)
        out=keras.layers.Dropout(0.4)(out)
     
        out = keras.layers.Dense(1024, activation="relu",kernel_regularizer=keras.regularizers.l2(0.01),
                                 kernel_initializer=keras.initializers.GlorotNormal())(out)
        out=keras.layers.Dropout(0.4)(out)
       
        outputs = keras.layers.Dense(1)(out)
    
        model = tf.keras.Model([state_input, action_input], outputs)

        return model

    def policy(self,state, noise,noise2):
        state=tf.expand_dims(tf.convert_to_tensor(state), 0)
        sampled_actions = tf.squeeze(self.actor_model(state))
        angular=sampled_actions[0]
        velocity=sampled_actions[1]
        #print("samlple",sampled_actions)
        
       
        # Adding noise to action
        angular = angular.numpy() + noise
        velocity=velocity.numpy() + noise2
        # We make sure action is within bounds
        angular = np.clip(angular, self.lower_bound, self.upper_bound)
        velocity = np.clip(velocity, 0.2, 0.5)
        #print(legal_action)

        return [np.squeeze(angular),np.squeeze(velocity)]
    
   



   

 

    # def load_data(self):
    #     self.actor_model = self.create_actor_model()
    #     self.target_actor = self.create_actor_model()
    #     self.critic_model = self.create_critic_model()
    #     self.target_critic = self.create_critic_model()
    #     path1 = os.path.join(self.dir_path, self.get_model_file_name("h5","actor"))
    #     path2 = os.path.join(self.dir_path, self.get_model_file_name("h5","target-actor"))
    #     path3 = os.path.join(self.dir_path, self.get_model_file_name("h5","critic"))
    #     path4 = os.path.join(self.dir_path, self.get_model_file_name("h5","target-critic"))
    #     self.actor_model = Utils.load_model(self.actor_model, path1)
    #     self.target_actor = Utils.load_model(self.target_actor, path2)
    #     self.critic_model = Utils.load_model(self.critic_model, path3)
    #     self.target_critic = Utils.load_model(self.target_critic, path4)
    #     path = os.path.join(self.dir_path, self.get_model_file_name("json"))
    #     self.buffer_counter=Utils.load_json(path, "counter")
        
    
    #     path = os.path.join(self.dir_path, self.get_model_file_name("obj","state"))
    #     self.state_buffer= Utils.load_pickle(path)
    #     path = os.path.join(self.dir_path, self.get_model_file_name("obj","reward"))
    #     self.reward_buffer= Utils.load_pickle(path)
    #     path = os.path.join(self.dir_path, self.get_model_file_name("obj","action"))
    #     self.action_buffer= Utils.load_pickle(path)
    #     path = os.path.join(self.dir_path, self.get_model_file_name("obj","next"))
    #     self.next_state_buffer= Utils.load_pickle(path)
    #     path = os.path.join(self.dir_path, self.get_model_file_name("obj","done"))
    #     self.dones= Utils.load_pickle(path)
       

    # def get_epsilon(self):
    #     return self.epsilon

    # def save_data(self, ep,reward):
    #     self.ep = ep
    #     path1 = os.path.join(self.dir_path, self.get_model_file_name("h5","actor"))
    #     path2 = os.path.join(self.dir_path, self.get_model_file_name("h5","target-actor"))
    #     path3 = os.path.join(self.dir_path, self.get_model_file_name("h5","critic"))
    #     path4 = os.path.join(self.dir_path, self.get_model_file_name("h5","target-critic"))
    #     actor = copy(self.actor_model)
    #     target_actor = copy(self.target_actor)
    #     critic = copy(self.critic_model)
    #     target_critic = copy(self.target_critic)
    #     #fix this the loss function
    #     actor.compile(optimizer=self.actor_optimizer, loss="custom_loss_actor")
    #     target_actor.compile(optimizer=self.actor_optimizer, loss="custom_loss_actor")
    #     critic.compile(optimizer=self.critic_optimizer, loss=loss_function)
    #     target_critic.compile(optimizer=self.critic_optimizer, loss=loss_function)
    #     Utils.save_model(actor, path1)
    #     Utils.save_model(target_actor, path2)
    #     Utils.save_model(critic, path3)
    #     Utils.save_model(target_critic, path4)
    #     path = os.path.join(self.dir_path, self.get_model_file_name("json"))
    #     data = {"reward":reward,"counter":self.buffer_counter}
    #     Utils.save_json(path, data)
       
    #     path = os.path.join(self.dir_path, self.get_model_file_name("obj","state"))
    #     Utils.save_pickle(path, self.state_buffer)
    #     path = os.path.join(self.dir_path, self.get_model_file_name("obj","reward"))
    #     Utils.save_pickle(path, self.reward_buffer)
    #     path = os.path.join(self.dir_path, self.get_model_file_name("obj","action"))
    #     Utils.save_pickle(path, self.action_buffer)
    #     path = os.path.join(self.dir_path, self.get_model_file_name("obj","next"))
    #     Utils.save_pickle(path, self.next_state_buffer)
    #     path = os.path.join(self.dir_path, self.get_model_file_name("obj","done"))
    #     Utils.save_pickle(path, self.dones)

    # def get_model_file_name(self, type,ext=None):
    #     return f"models-{self.name}/my-model-{self.ep}-{ext}.{type}"
      