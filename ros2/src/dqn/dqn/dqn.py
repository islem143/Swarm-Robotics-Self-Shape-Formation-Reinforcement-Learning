import rclpy

from rclpy.node import Node
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
import numpy as np
from gazebo_msgs.srv import DeleteEntity
from gazebo_msgs.srv import SpawnEntity
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile
import tensorflow as tf
from tensorflow import keras
from dqn_msg.srv import Dqnn

from collections import deque

import os
from keras.callbacks import TensorBoard
import random
import time


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


class Dqn(Node):

    def __init__(self):
        super().__init__('dqn')
        self.model = self.create_model()
        self.target_model = self.model
        #self.dqn_sub = self.create_subscription(State, "/state", self.dqn, 10)
        self.actions = [-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2]
        self.actions_size = 5
        self.state_size = 3
        self.discout_factor = 0.99
        self.minbatch_size = 64
        self.episode_length = 10_000
        self.steps_per_episode = 1000
        self.replay_memory = deque(maxlen=50_000)
        self.episode_size = 3000
        self.target_update_counter = 0
        self.epsilon = 1  # not a constant, going to be decayed
        self.EPSILON_DECAY = 0.99975
        self.MIN_EPSILON = 0.001
        self.MIN_REPLAY_MEMORY_SIZE = 1_000
        self.env_result_client = self.create_client(Dqnn, "env_result")
        self.start()

    def start(self):
        i = 0
        for _ in range(self.episode_length):
            time.sleep(2)
            self.req = Dqnn.Request()
            self.req.init = True
            self.req.action = 0
            future = self.env_result_client.call_async(self.req)
            rclpy.spin_until_future_complete(self, future)
            self.current_state = future.result().state
            done = False
            while not done:
                while not self.env_result_client.wait_for_service(timeout_sec=1.0):
                    self.get_logger().info('service not available, waiting again...')
                self.req = Dqnn.Request()
                self.req.init = False
                if np.random.random() > self.epsilon:
                    action = np.argmax(self.get_action(self.current_state))
                else:
                    action = np.random.randint(0, self.actions_size)

                self.req.action = action
                future = self.env_result_client.call_async(self.req)
                rclpy.spin_until_future_complete(self, future)
                state = future.result().state
                reward = future.result().reward
                done = future.result().done
                i += 1
                if (i == self.steps_per_episode):
                    done = True
                time.sleep(0.01)

    def get_action(self, state):
        return self.model.predict(state)[0]

    def create_model(self):
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(3,)),
            keras.layers.Dense(256, activation="relu"),
            keras.layers.Dense(256, activation="relu"),
            keras.layers.Dense(5, activation="sigmoid")
        ])

        model.compile(optimizer=keras.optimizers.Adam(
            learning_rate=0.1), loss="mse", metrics=["accuracy"])
        return model

    def train(self, terminal_state):
        if (self.MIN_REPLAY_MEMORY_SIZE > len(self.replay_memory)):
            return

        minibatch = random.sample(self.replay_memory, self.minbatch_size)

        current_states = np.array([batch[0] for batch in minibatch])/255
        next_states = np.array([batch[3] for batch in minibatch])/255
        q_values = self.model.predict(current_states)
        next_q_values = self.target_model.predict(next_states)
        X = []
        y = []
        for index, (current_state, reward, action, next_state, done) in enumerate(minibatch):

            if not done:
                new_q = reward+self.discout_factor*np.max(next_q_values[index])
            else:
                new_q = reward

            q_values[index][action] = new_q
            X.append(current_state)
            y.append(q_values)
            self.model.fit(np.array(X)/255, np.array(y), batch_size=self.minbatch_size, verbose=0,
                           shuffle=False, callbacks=[self.tensorboard] if terminal_state else None)
            if terminal_state:
                self.target_update_counter += 1

        # If counter reaches set value, update target network with weights of main network
            if self.target_update_counter > 5:
                self.target_model.set_weights(self.model.get_weights())
                self.target_update_counter = 0

    def get_q_value(self, state):
        return self.model.predict(state/255)[0]

    def dqn(self, msg):
        pass


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
