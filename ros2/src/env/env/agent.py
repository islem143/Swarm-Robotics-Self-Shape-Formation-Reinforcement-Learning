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
from dqn_msg.srv import Reach
from dqn_msg.msg import Goal
import time
import threading
from dqn.ac_network import ACNetwork
num_agents=4

class Agent(Node):
    def __init__(self,id):
        super().__init__(f'agent{id}')
        self.id=int(id)
        self.cmd_vel_pub = self.create_publisher(
                Twist, f'/t{self.id}/cmd_vel', 10)
        self.get_odom = self.create_subscription(
            Odometry, f"/t{self.id}/odom", self.get_current_position, 10)
        
        self.get_laser = self.create_subscription(
            LaserScan, f"/t{self.id}/scan", self.get_lds, 10)
       

        self.agent=ACNetwork(f"robot-{self.id}",True,1000)
        if(self.id==4):
            self.agent=ACNetwork(f"robot-1",True,1000)
        self.position=[0.0,0.0]
        self.goal_position=[-1.0,-1.0]
        self.angle=0.0
        self.goal_angle=0.0
        self.min_lds_angle=0.0
        self.min_lds_dist=3.5
        self.task_finished=False
        if(self.id==1):
            self.goal_publisher=self.create_publisher(Goal,"generate_goa",10) 
            self.reached_service=self.create_service(Reach,"reach_goal",self.goal_reached)
            
            #self.create_timer(2,self.pub_goal)
            self.start()
            
           
            
        else:
            self.position_leader=[0.0,0.0]
            #self.create_subscription(
            #Goal, "generate_goa", self.get_goal, 10)  
            self.get_odom_leader = self.create_subscription(
            Odometry, f"/t1/odom", self.get_current_position_leader, 10)
           # self.goal_position=[0.0,1.5] 
            self.create_timer(0.2,self.cc)
            self.reached_client = self.create_client(Reach, "reach_goal")
            self.start()
            
           # print(self.goal_cords)
           
      
        
        
    def get_current_position_leader(self,msg):
        

        self.position_leader = [
            msg.pose.pose.position.x, msg.pose.pose.position.y]
        
     
      
       
    def pub_goal(self):
        msg = Goal()                                               
        msg.goal = [self.goal_position[0],self.goal_position[1],1.5,0.0,3.0,0.0,1.5,np.pi]        
        self.goal_publisher.publish(msg)

    def cc(self):
            deg=45
            if(self.id==3):
                deg=220.0
            if(self.id==2):
                deg=120.0

            x=1.5*np.sin(deg)
            y=1.5*np.cos(deg) 
            if(self.id==3):
                print(x,y)
            self.goal_position=[self.position_leader[0]+x,self.position_leader[1]+y]      
        
    def goal_reached(self,request,response):

        print("goal reached by request id",request.id)
        response.ack=True
        return response   
    
    def start(self):
         while rclpy.ok():
           
            rclpy.spin_once(self)
            
            state=self.get_state()
         
            
            result=self.agent.policy(state, 0,0)
            
            self.move_robots(float(result[0]),float(result[1]))
            if(self.get_distance(self.position,self.goal_position)<0.20):
                print("goal reached")
                if(self.id!=1):
                   
                    self.send_task()
                self.stop_robot()    
                break
            #time.sleep(0.05)

    def send_task(self):
        req = Reach.Request()
        req.id = self.id
        future = self.reached_client.call_async(req)
        while rclpy.ok():
            rclpy.spin_once(self)
            if future.done():
                if future.result() is not None:
                    
                
                        res = future.result(
                        ).ack
                        print("ack",res)
                        
                else:
                    self.get_logger().error(
                        'Exception while calling service: {0}'.format(future.exception()))
                break
    def get_state(self):
        
        l = list()
       
        
        l.append(float(self.get_distance(self.position,self.goal_position)))
        l.append(float(self.goal_angle))
        l.append(float(self.min_lds_dist))
        l.append(float(self.min_lds_angle))

    
           


        return l

    def move_robots(self,ang,velo):
        twist = Twist()
        twist.linear.x = velo
        twist.angular.z = ang
        self.cmd_vel_pub.publish(twist)

    def stop_robot(self):
        self.cmd_vel_pub.publish(Twist())
    def get_goal(self,msg):
         d,theta=msg.goal[2*(self.id-1):2*(self.id-1)+2]
         x=d*np.sin(theta)
         y=d*np.cos(theta)
         
         self.goal_position=[msg.goal[0]+x,msg.goal[1]+y]
         if(self.id==4):
             print(self.goal_position)
    
         print(self.id,d,theta)
         
         
    def get_distance(self, p1, p2):
        return float(np.sqrt(np.square(
            p1[1]-p2[1])+np.square(p1[0]-p2[0])))
      
    def get_lds(self, msg):
        
        self.min_lds_dist = np.min(msg.ranges)
        if (self.min_lds_dist == np.Inf):
            self.min_lds_dist = float(3.5)
        self.min_lds_angle = np.argmin(msg.ranges)

    def get_current_position(self, msg):
        
        
        
        self.position = [
            msg.pose.pose.position.x, msg.pose.pose.position.y]
        self.angle = self.euler_from_quaternion(
            msg.pose.pose.orientation)[2]
     
      
        self.goal_angle = (np.arctan2(self.goal_position[1]-self.position
                               [1], self.goal_position[0]-self.position[0]))-(self.angle)

        if (self.goal_angle > np.pi):
            self.goal_angle -= 2*np.pi
        elif (self.goal_angle < -np.pi):
            self.goal_angle += 2*np.pi    

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

