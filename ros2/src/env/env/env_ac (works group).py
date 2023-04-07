import rclpy

from rclpy.node import Node
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
import numpy as np
import random

from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile
from std_srvs.srv import Empty

from dqn_msg.srv import Mac
from dqn_msg.msg import Goal
import time


class Env(Node):

    def __init__(self):
        super().__init__('env')
        self.num_agents=4
        self.cmd_vel_pub = {}
        self.goal_reached_by={}
        for i in range(self.num_agents):
            self.cmd_vel_pub[i] = self.create_publisher(
                Twist, f'/t{i+1}/cmd_vel', 10)
            self.goal_reached_by[i]=0
        self.get_odom = self.create_subscription(
            Odometry, "/t1/odom", self.get_current_position, 10)
        self.get_laser = self.create_subscription(
            LaserScan, "/t1/scan", self.get_lds, 10)
        self.get_odom2 = self.create_subscription(
            Odometry, "/t2/odom", self.get_current_position2, 10)
        self.get_laser2 = self.create_subscription(
            LaserScan, "/t2/scan", self.get_lds2, 10)
        self.get_odom3 = self.create_subscription(
            Odometry, "/t3/odom", self.get_current_position3, 10)
        self.get_laser3 = self.create_subscription(
             LaserScan, "/t3/scan", self.get_lds3, 10)
        self.get_odom4 = self.create_subscription(
            Odometry, "/t4/odom", self.get_current_position4, 10)
        self.get_laser4 = self.create_subscription(
            LaserScan, "/t4/scan", self.get_lds3, 10)
        self.test=False
        self.env_result_service = self.create_service(
            Mac, "env_result", self.step)
        # self.env_goal_service = self.create_service(
        #     Goal, "goal_pose", self.generate_goal_pose)
        self.reset_sim_client = self.create_client(Empty, "reset_sim")
        self.goal_publisher=self.create_publisher(Goal,"generate_goal",10) 
        self.shapes={
            "line":[[0.0,1.0],[0.0,2.0] ,[0.0,-1.0],[0.0,0.0]],
            "line2":[[1.0,0.0],[2.0,0.0] ,[-1.0,0.0],[-2.0,0.0]],
            "trianlge":[[0.0,0.0],[0.0,1.2] ,[0.0,-1.2],[1.2,0.0]],
            "trianlge2":[[0.0,1.5],[0.0,0.0] ,[0.0,-1.2],[1.5,0.0]],
            "square":[[-1.2,-1.2],[1.2,1.2] ,[-1.2,1.2],[1.2,-1.2]],
            "line3":[[2.5,2.5],[1.5,1.5] ,[0.5,0.5],[-0.5,-0.5]],
           

        }
        self.goal_cords = self.shapes["line2"]
        
        self.dones = [False for _ in range(self.num_agents)]

        self.steps = 0
        self.fails = [False for _ in range(self.num_agents)]

        self.succeses = [False for _ in range(self.num_agents)]
        self.positions = [[0, 0] for _ in range(self.num_agents)]
        self.min_ldss_dist = [3.5 for _ in range(self.num_agents)]
        self.min_ldss_angle = [3.5 for _ in range(self.num_agents)]
        self.angles = [3.5 for _ in range(self.num_agents)]
        self.goal_angles = [0.0 for _ in range(self.num_agents)]
        self.init_positions = [[0, 0] for _ in range(self.num_agents)]
        self.global_steps=0
        
       
 

    def get_current_position(self, msg):
        self.positions[0] = [
            msg.pose.pose.position.x, msg.pose.pose.position.y]
        self.angles[0] = self.euler_from_quaternion(
            msg.pose.pose.orientation)[2]
        #self.goal_angles[0] = self.get_goal_angle(0)

        self.goal_angles[0] = (np.arctan2(self.goal_cords[0][1]-self.positions[0]
                               [1], self.goal_cords[0][0]-self.positions[0][0]))-(self.angles[0])

        if (self.goal_angles[0] > np.pi):
            self.goal_angles[0] -= 2*np.pi
        elif (self.goal_angles[0] < -np.pi):
            self.goal_angles[0] += 2*np.pi
        #print(self.get_distance(self.positions[0],self.positions[1]))
        print(np.arctan2(np.abs(self.positions[0][0]-self.positions[1][0]),np.abs(self.positions[0][1]-self.positions[1][1])))
        
        


       

    def get_current_position2(self, msg):
        self.positions[1] = [
            msg.pose.pose.position.x, msg.pose.pose.position.y]
        self.angles[1] = self.euler_from_quaternion(
            msg.pose.pose.orientation)[2]

        self.goal_angles[1] = (np.arctan2(self.goal_cords[1][1]-self.positions[1]
                               [1], self.goal_cords[1][0]-self.positions[1][0]))-(self.angles[1])
        if (self.goal_angles[1] > np.pi):
            self.goal_angles[1] -= 2*np.pi
        elif (self.goal_angles[1] < -np.pi):
            self.goal_angles[1] += 2*np.pi
          
    def get_current_position3(self, msg):
        self.positions[2] = [
            msg.pose.pose.position.x, msg.pose.pose.position.y]
        self.angles[2] = self.euler_from_quaternion(
            msg.pose.pose.orientation)[2]
            
        self.goal_angles[2] = (np.arctan2(self.goal_cords[2][1]-self.positions[2]
                               [1], self.goal_cords[2][0]-self.positions[2][0]))-(self.angles[2])
        if (self.goal_angles[2] > np.pi):
            self.goal_angles[2] -= 2*np.pi
        elif (self.goal_angles[2] < -np.pi):
            self.goal_angles[2] += 2*np.pi
    def get_current_position4(self, msg):
        self.positions[3] = [
            msg.pose.pose.position.x, msg.pose.pose.position.y]
        self.angles[3] = self.euler_from_quaternion(
            msg.pose.pose.orientation)[2]

        self.goal_angles[3] = (np.arctan2(self.goal_cords[3][1]-self.positions[3]
                               [1], self.goal_cords[3][0]-self.positions[3][0]))-(self.angles[3])
        if (self.goal_angles[3] > np.pi):
            self.goal_angles[3] -= 2*np.pi
        elif (self.goal_angles[3] < -np.pi):
            self.goal_angles[3] += 2*np.pi   

    def get_lds(self, msg):

        self.min_ldss_dist[0] = np.min(msg.ranges)
        if (self.min_ldss_dist[0] == np.Inf):
            self.min_ldss_dist[0] = float(4)
        self.min_ldss_angle[0] = np.argmin(msg.ranges)
       
        
        
        

    def get_lds2(self, msg):

        self.min_ldss_dist[1] = np.min(msg.ranges)
        if (self.min_ldss_dist[1] == np.Inf):
            self.min_ldss_dist[1] = float(4)
        self.min_ldss_angle[1] = np.argmin(msg.ranges)

    def get_lds3(self, msg):

        self.min_ldss_dist[2] = np.min(msg.ranges)
        if (self.min_ldss_dist[2] == np.Inf):
            self.min_ldss_dist[2] = float(4)
        self.min_ldss_angle[2] = np.argmin(msg.ranges) 
    def get_lds4(self, msg):

        self.min_ldss_dist[3] = np.min(msg.ranges)
        if (self.min_ldss_dist[3] == np.Inf):
            self.min_ldss_dist[3] = float(4)
        self.min_ldss_angle[3] = np.argmin(msg.ranges)


   
    def init_robots(self, index):

        twist = Twist()
        twist.linear.x = 0.4
        self.cmd_vel_pub[index].publish(twist)

    def move_robots(self, action, index):
        twist = Twist()
        twist.linear.x = 0.4
        twist.angular.z = action
        self.cmd_vel_pub[index].publish(twist)

    def stop_robots(self, index):
        self.cmd_vel_pub[index].publish(Twist())

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

    def call_reset_sim(self):
        
        req = Empty.Request()
        while not self.reset_sim_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.reset_sim_client.call_async(req)

    def step(self, request, response):
        if (request.init):
            self.steps = 0
            self.dones = [False for _ in range(self.num_agents)]
            for index in range(self.num_agents):
                self.init_positions[index] = self.positions[index]

                self.init_robots(index)
                print(self.goal_cords)
            response.states = self.get_state()

            return response

       
       
        #self.dones = [False for _ in range(self.num_agents)]
        actions = request.actions

        for index in range(self.num_agents):
            action = actions[index]
           
            self.move_robots(action, index)

        state_s = self.get_state()
        rewards = self.get_reward()

        response.states = state_s
        response.rewards = rewards

        response.dones = self.dones
        return response

    def get_distance_to_goal(self, index):
        return float(np.sqrt(np.square(self.positions[index][1]-self.goal_cords[index][1])+np.square(self.positions[index][0]-self.goal_cords[index][0])))
    
    def shape_formed(self):
        for i in range(self.num_agents):
            if(not self.goal_reached(i)):
                return False
        return True    
            
    def generate_goal_pose(self):
        #x = float(np.random.randint(-0.5, 2.2))
        #y = float(np.random.randint(-2.2, 2.2))

        #xx=[2.0,0.5,1.5,0.0,-2.0]
        #yy=[2.0,0.5,1.5,0.0,-2.0]
        a=["line","trianlge","square","line2","trianlge2","line3"]
        chosen=random.choice(a)
        self.goal_cords=self.shapes[chosen]
        print("chosen shape",chosen)
        print(self.goal_cords)
        
        # for i in range(self.num_agents):
        #     #x=np.random.choice(xx)
        #     #y=np.random.choice(yy)
        #     if(self.goal_reached_by[i]>=1):
        #         # a=["line","trianlge","square"]
        #         # chosen=random.choice(a)
        #         # print("chosen shape",chosen)
        #         # self.goal_cords=self.shapes[chosen]

               
        #         self.goal_cords[i][0]=x
        #         self.goal_cords[i][1]=y
        #         msg = Goal()                                               
        #         msg.goal = [x,y]                                          
        #         self.goal_publisher.publish(msg)
        #         self.goal_reached_by[i]=0

       
       
        
        

    def crashs(self, index):
     
        if (self.min_ldss_dist[index] < 0.13):

            return True
        return False

    
    def get_abs_distance_to_goal(self, index):
        return float(np.sqrt(np.square(self.init_positions[index][1]-self.goal_cords[index][1])+np.square(self.init_positions[index][0]-self.goal_cords[index][0])))

    def goal_reached(self, index):
        distance = self.get_distance_to_goal(index)

        if (distance < 0.2):

            return True
        return False
    def get_distance(self, p1, p2):
        return float(np.sqrt(np.square(
            p1[1]-p2[1])+np.square(p1[0]-p2[0])))

   

    def get_reward(self):
        rewards = [0 for _ in range(self.num_agents)]
        for index in range(self.num_agents):
            distance = self.get_distance_to_goal(index)
            rewards[index] += -(distance/self.get_abs_distance_to_goal(index))+1

            rewards[index] += -np.abs(self.goal_angles[index])+0.2
            
            if (self.min_ldss_dist[index] < 0.55):
                rewards[index] -= 10
        
            if self.succeses[index]:
                rewards[index] += 500
            elif self.fails[index]:
                rewards[index] -= 500
    
        return rewards
       

    def get_state(self):
        l = list()
        self.global_steps+=1
        self.succeses = [False for _ in range(self.num_agents)]
        self.fails = [False for _ in range(self.num_agents)]
        for index in range(self.num_agents):
            
            norm_angle = (self.goal_angles[index]+3.14)/(3.14+3.14)
            distance = self.get_distance_to_goal(index)
            norm_goal = distance/6.22
            norm_lds = (self.min_ldss_dist[index]-0)/(3.5)
            norm_lds_angle = self.min_ldss_angle[index]
           
            # l.append(float(norm_goal))
            # l.append(float(norm_angle))
            # l.append(float(norm_lds))
            # l.append(float(norm_lds_angle))
            
            l.append(float(self.get_distance_to_goal(index)))
            l.append(float(self.goal_angles[index]))
            l.append(float(self.min_ldss_dist[index]))
            l.append(float(self.min_ldss_angle[index]))
            if (self.crashs(index)):
                 if(self.test):
                     self.dones = [True for _ in range(self.num_agents)]
                     self.fails = [True for _ in range(self.num_agents)]
                 else:     
                    #if(not self.global_steps<5000):
                    
                        self.dones = [True for _ in range(self.num_agents)]
                        self.fails[index] = True
                        self.steps = 0
                    # else:
                    #     self.dones[index]=True  
                    #     self.fails[index] = True
                    #     self.stop_robots(index) 
                

            if (self.goal_reached(index)):
                self.goal_reached_by[index]+=1
                self.succeses[index] = True
                self.dones[index] = True
                self.stop_robots(index)
               

            if (self.steps == 550 and not self.test):
                self.dones = [True for _ in range(self.num_agents)]
                self.fails = [True for _ in range(self.num_agents)]
                if self.succeses[index]:
                    self.fails[index] = False
                self.steps = 0
          
            

        if (all(self.dones)):
            for index in range(self.num_agents):
                self.stop_robots(index)
            self.call_reset_sim()
            if(all(self.succeses)):
                self.generate_goal_pose()
        self.steps += 1
     
      
        return l
        # else:
        #     l.append(self.get_distance_to_goal(self.goal_cord2,2))
        #     l.append(float(self.min_lds_dist2))
        #     l.append(float(self.goal_angle2))
        #     return l


def main(args=None):
    rclpy.init(args=args)

    env = Env()

    rclpy.spin(env)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    env.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()