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
from dqn_msg.msg import State
from collections import deque
import os
from keras.callbacks import TensorBoard

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
        self.dqn_sub = self.create_subscription(State, "/state", self.dqn, 10)
        self.actions = [-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2]
        self.actions_size = 5
        self.state_size = 4
        self.replay_memory = deque(maxlen=50_000)
        self.episode_size = 3000
        self.target_update_counter = 0

       
       

    def create_model(self):
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(4,)),
            keras.layers.Dense(256, activation="relu"),
            keras.layers.Dense(256, activation="relu"),
            keras.layers.Dense(5, activation="sigmoid")
        ])
        model.compile(optimizer=keras.optimizers.Adam(
            learning_rate=0.1), loss="mse", metrics=["accuracy"])
        return model

    def train(self):
        
        pass

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
