import rclpy
import sys
from rclpy.node import Node
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
import numpy as np
import random
from rclpy.executors import MultiThreadedExecutor

from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile
from std_srvs.srv import Empty

from dqn_msg.srv import Mac
from dqn_msg.msg import Goal
import time
import threading

num_agents=4

class Agent(Node):
    def __init__(self,id):
        super().__init__(f'agent{id}')
        self.id=int(id)
        self.cmd_vel_pub = self.create_publisher(
                Twist, f'/t{id}/cmd_vel', 10)
        self.get_odom = self.create_subscription(
            Odometry, f"/t{id}/odom", self.get_current_position, 10)
       
        # self.get_laser = self.create_subscription(
        #     LaserScan, f"/t{id}/scan", self.get_lds, 10)
    
        if(self.id==1):
            self.goal_publisher=self.create_publisher(Goal,"generate_goa",10) 
            msg = Goal()                                               
            msg.goal = [0.0,0.0,1.5,0.0,1.5,180.0,1.5,90.0]        
            self.goal_publisher.publish(msg)
           
            
        else:
            print(self.id)
            self.create_subscription(
            Goal, "generate_goa", self.get_goal, 10)    
        self.position=[0.0,0.0]
        self.angle=0.0
        self.goal_angle=0.0
      
        
        
       


    def get_goal(self,msg):
   
        print("msg",msg)

    def get_current_position(self, msg):
        
        
        
        self.position = [
            msg.pose.pose.position.x, msg.pose.pose.position.y]
        self.angle = self.euler_from_quaternion(
            msg.pose.pose.orientation)[2]
     
      
        # #self.goal_angle = (np.arctan2(self.goal_cords[0][1]-self.positions[0]
        # #                       [1], self.goal_cords[0][0]-self.positions[0][0]))-(self.angles[0])

        # if (self.goal_angles[0] > np.pi):
        #     self.goal_angles[0] -= 2*np.pi
        # elif (self.goal_angles[0] < -np.pi):
        #     self.goal_angles[0] += 2*np.pi    

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

    agent = Agent(sys.argv[2])
   
    rclpy.spin(agent)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    agent.destroy_node()
    rclpy.shutdown()

# def main(args=None):
#     rclpy.init(args=args)
#     agents=[]
#     executor = MultiThreadedExecutor()
#     for i in range(num_agents):
#          agents.append(Agent(i+1))
#          executor.add_node(agents[-1])

        
   
   
   
        
#     thread = threading.Thread(target=executor.spin)
#     thread.start()


        


     
    
#     rate = agents[0].create_rate(2)
#     try:
#         while rclpy.ok():
#             print('Help me body, you are my only hope')
#             rate.sleep()
#     except KeyboardInterrupt:
#      pass
    
        
#     for agent in agents:    
#         agent.destroy_node()    
   

   

   
    
#     rclpy.shutdown()
#     thread.join()    

if __name__ == '__main__':
    main()

