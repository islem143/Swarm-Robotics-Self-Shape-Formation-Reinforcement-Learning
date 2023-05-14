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
import time
from dqn_msg.msg import Goal


class Gazebo(Node):
     

    def __init__(self):
        super().__init__('gazebo')
        qos = QoSProfile(depth=10)
        self.goal_pose_x=1.5
        self.goal_pose_y=1.5
        self.spawn_entity_client = self.create_client(SpawnEntity, 'spawn_entity')
        self.delete_entity_client = self.create_client(DeleteEntity, 'delete_entity')
       # self.create_subscription(
       #     Goal, "generate_goal", self.get_goal, 10)
        self.reset_simulation_client = self.create_client(Empty, 'reset_simulation')
        #self.init_service = self.create_service(Dqn, 'init', self.dqn_com_callback)
        self.position_x=1.0
        self.position_y=-1.0
        
        self.goal_entity_name="goal"
        entity_path = '/home/islem/Documents/PFE/ros2/model.sdf'
        self.goal_xml=open(entity_path, 'r').read()
        self.reset_sim_service=self.create_service(Empty,"reset_sim",self.reset_simulations)
   
        #self.delete_entity(self.goal_entity_name)
        #self.init()
        #self.delete_entity(self.goal_entity_name)
        #self.create_timer(0.5,self.spawn)
        
    def spawn(self):
        self.spawn_entity(self.goal_entity_name,self.goal_xml)

    def get_goal(self,msg):
        #self.delete_entity(self.goal_entity_name)
        
        self.position_x=msg.goal[0]
        self.position_y=msg.goal[1]
        
        

    #def init(self):
        
        
        #self.spawn_entity(self.goal_entity_name,self.goal_xml)
        


    def reset_simulations(self,request,response):
  
        req = Empty.Request()
        while not self.reset_simulation_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.reset_simulation_client.call_async(req)
        
        #self.delete_entity(self.goal_entity_name)
        time.sleep(0.2)
        #self.spawn_entity(self.goal_entity_name,self.goal_xml)
        return response
        

    def generate_goal_pose(self):
        x=float(np.random.randint(-4,4))
        y=float(np.random.randint(-4,4))
        return x,y

    def spawn_entity(self,name,xml):
        #print("spawned")
        goal_pose = Pose()
       
        goal_pose.position.x = self.position_x 
        goal_pose.position.y = self.position_y
        req = SpawnEntity.Request()
        req.name = name
        req.xml = xml
        req.initial_pose = goal_pose
        while not self.spawn_entity_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.spawn_entity_client.call_async(req)

    def delete_entity(self,name):
        print("deleted")
        req = DeleteEntity.Request()
        req.name = name
        while not self.delete_entity_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
      
        self.delete_entity_client.call_async(req)          
   

    

def main(args=None):
    rclpy.init(args=args)

    gazebo = Gazebo()

    rclpy.spin(gazebo)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gazebo.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


     
