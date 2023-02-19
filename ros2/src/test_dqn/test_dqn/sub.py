# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
from std_srvs.srv import Empty

class MinimalSubscriber(Node):
   
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.entity_path = '/home/islem/Documents/PFE/ros2/model.sdf'
        self.entity = open(self.entity_path, 'r').read()
        self.entity_name = 'goal'

        self.goal_pose_x=3.0
        self.goal_pose_y=3.0
        self.spawn_entity_client = self.create_client(SpawnEntity, 'spawn_entity')
        
        self.publish_timer = self.create_timer(
            1,  # unit: s
            self.publish_callback)
        qos = QoSProfile(depth=10)
        self.move_robot=self.create_publisher(Twist, "/t1/cmd_vel",qos)  
        self.reset_simulation_client = self.create_client(Empty, 'reset_simulation')
        # msg=Twist()
        # msg.linear.x=0.5
        # msg.angular.z=1.57
        # self.move_robot.publish(msg)
        # self.subscription = self.create_subscription(
        #      LaserScan,
        #     't2/scan',
        #     self.listener_callback,
        #     10)

        #self.subscription  # prevent unused variable warning
    def reset_simulation(self):
        req = Empty.Request()
        while not self.reset_simulation_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.reset_simulation_client.call_async(req)
    
    def publish_callback(self):
        random_x=float(np.random.randint(0,5))
        random_y=float(np.random.randint(0,5))
        self.goal_pose_x=random_x
        self.goal_pose_y=random_y
      
       # self.delete_entity()
       # self.spawn_entity()
       
        #self.move_robot.publish(Twist())

    def listener_callback(self, msg):
        self.get_logger().info(f"{msg.ranges}")
        self.spawn_entity()
        #self.get_logger().info(f"{self.euler_from_quaternion(msg.pose.pose.orientation)}")
        # path_theta = math.atan2(
        #     self.goal_pose_y-self.last_pose_y,
        #     self.goal_pose_x-self.last_pose_x)
        #current_frame = self.br.imgmsg_to_cv2(msg)
    
        # Display image
        #cv2.imshow("camera", current_frame)
    
        #cv2.waitKey(1)
    def spawn_entity(self):
        goal_pose = Pose()
        goal_pose.position.x = self.goal_pose_x
        goal_pose.position.y = self.goal_pose_y
        req = SpawnEntity.Request()
        req.name = self.entity_name
        req.xml = self.entity
        req.initial_pose = goal_pose
        while not self.spawn_entity_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.spawn_entity_client.call_async(req)
        
    def euler_from_quaternion(self, quat):
        """
        Converts quaternion (w in last place) to euler roll, pitch, yaw
        quat = [x, y, z, w]
        """
        x = quat.x
        y = quat.y
        z = quat.z
        w = quat.w

        sinr_cosp = 2 * (w*x + y*z)
        cosr_cosp = 1 - 2*(x*x + y*y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)

        sinp = 2 * (w*y - z*x)
        pitch = np.arcsin(sinp)

        siny_cosp = 2 * (w*z + x*y)
        cosy_cosp = 1 - 2 * (y*y + z*z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)

        return roll, pitch, yaw    
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()