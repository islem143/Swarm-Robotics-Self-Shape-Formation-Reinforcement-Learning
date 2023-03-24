import rclpy

from rclpy.node import Node
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
import numpy as np


from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile
from std_srvs.srv import Empty

from dqn_msg.srv import Dqnn
from dqn_msg.srv import Goal
import time


class Env(Node):

    def __init__(self):
        super().__init__('env')
        self.num_agents = 2
     
        self.cmd_vel_pub = {}

        self.create_subscription(
                Odometry, f"/t1/odom", self.get_current_position, 10)
        self.create_subscription(
                Odometry, f"/t2/odom", self.get_current_position2, 10)
             
        self.create_subscription(
                LaserScan, f"/t1/scan", self.get_lds, 10)
        self.create_subscription(
                LaserScan, f"/t2/scan", self.get_lds2, 10)
        for i in range(self.num_agents):
            self.cmd_vel_pub[i] = self.create_publisher(
                    Twist, f'/t{i}/cmd_vel', 10)

        self.env_result_service = self.create_service(
            Dqnn, "env_result", self.step)
        self.env_goal_service = self.create_service(
            Goal, "goal_pose", self.generate_goal_pose)
        self.reset_sim_client = self.create_client(Empty, "reset_sim")

        self.goal_cords = [[0.01, 0.01], [0.01, 0.01-1]]
        self.done = False

        self.steps = 0
        self.fails = []
        self.succeses = []
        self.positions = []
        self.min_ldss_dist=[]
        self.min_ldss_angle=[]
        self.angles = []
        self.goal_angles = []
        self.init_positions = []

    def get_current_position(self, msg):
        self.positions[0]=[msg.pose.pose.position.x,msg.pose.pose.position.y]
        self.angles[0]=self.euler_from_quaternion(msg.pose.pose.orientation)[2]
        self.goal_angles[0]=self.get_goal_angle(0)
       
   
    def get_current_position2(self, msg):
        self.positions[1]=[msg.pose.pose.position.x,msg.pose.pose.position.y]
        self.angles[1]=self.euler_from_quaternion(msg.pose.pose.orientation)[2]
        self.goal_angles[1]=self.get_goal_angle(1)

    def get_lds(self, msg):

      
        self.min_ldss_dist[0]=np.min(msg.ranges)
        if (self.min_ldss_dist[0] == np.Inf):
            self.min_ldss_dist[0] = float(4)
        self.min_ldss_angle[0] = np.argmin(msg.ranges)

    def get_lds2(self, msg):

      
        self.min_ldss_dist[1]=np.min(msg.ranges)
        if (self.min_ldss_dist[0] == np.Inf):
            self.min_ldss_dist[1] = float(4)
        self.min_ldss_angle[1] = np.argmin(msg.ranges)

    def get_goal_angle(self,index):
        if (self.positions[index][0] > self.goal_cords[index][0] and self.positions[index][1] > self.goal_cords[index][1]):

            return np.abs(self.angles[index]-(np.arctan2(np.abs(self.positions[index][1]-self.goal_cords[index][1]), np.abs(self.positions[index][0]-self.goal_cords[index][0]))-np.pi))
        elif (self.positions[index][0] < self.goal_cords[index][0] and self.positions[index][1] < self.goal_cords[index][1]):
            return np.abs(self.angles[index]-(np.arctan2(np.abs(self.positions[index][1]-self.goal_cords[index][1]), np.abs(self.positions[index][0]-self.goal_cords[index][0]))))
        elif (self.positions[index][0] > self.goal_cords[index][0] and self.positions[index][1] < self.goal_cords[index][1]):
            return np.abs(self.angles[index]-(np.arctan2(np.abs(self.positions[index][0]-self.goal_cords[index][0]), np.abs(self.positions[index][1]-self.goal_cords[index][1]))+np.pi/2))
        else:
            return np.abs(self.angles[index]-(np.arctan2(np.abs(self.positions[index][0]-self.goal_cords[index][0]), np.abs(self.positions[index][1]-self.goal_cords[index][1]))-np.pi/2))
   
    def init_robots(self,index):

        twist = Twist()
        twist.linear.x = 0.3
        self.cmd_vel_pub[index].publish(twist)
     
    def move_robots(self, action,index):
        twist = Twist()
        twist.linear.x = 0.3
        twist.angular.z = action
        self.cmd_vel_pub[index].publish(twist)
  
    def stop_robots(self,index):
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
        for i in range(self.num_agents):
            self.stop_robots(i)
        
        req = Empty.Request()
        while not self.reset_sim_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.reset_sim_client.call_async(req)

    def get_abs_distance_to_goal(self,index):
        return float(np.sqrt(np.square(self.init_position[1]-self.goal_cords[index][1])+np.square(self.init_position[0]-self.goal_cords[index][0])))

    def step(self, request, response):
        index=request.id
        if (request.init):
            response.state = self.get_state(index)
            self.init_positions[index] =self.positions[index]

            return response

        actions_index = int(request.action)
        self.done = False
        actions = [-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2]
        action = float(actions[actions_index])

        if (request.id == 1):
            self.move_robot(action)

        else:
            self.move_robot2(action)

        state_s = self.get_state(request.id)
        reward = self.get_reward(request.id)

        response.state = state_s
        response.reward = reward
        response.done = self.done
        return response

    def get_distance_to_goal(self, index):
        return float(np.sqrt(np.square(self.positions[index][1]-self.goal_cords[index][1])+np.square(self.positions[index][0]-self.goal_cords[index][0])))
      

    def generate_goal_pose(self):
        x = float(np.random.randint(-4, 4))
        y = float(np.random.randint(-4, 4))
        self.goal_x = x
        self.goal_y = y
        return x, y
    
    def crashs(self,index):
        if (self.min_ldss_dist[index] < 0.13):

            return True
        return False
    
    

  

    def goal_reached(self,index):
        distance = self.get_distance_to_goal(index)

        if (distance < 0.20):
            

            return True
        return False


    def get_reward(self, id):
        reward = 0.0
        if (id == 1):
            distance = self.get_distance_to_goal(self.goal_cord, 1)
            reward += -(distance/self.get_abs_distance_to_goal())

            if (self.goal_angle < 0.40):
                reward += 5
            print(reward)

            if self.success:
                reward += 100
            elif self.fail:
                reward -= 100

        else:
            distance = self.get_distance_to_goal(self.goal_cord2, 2)
            reward += -(distance/self.get_abs_distance_to_goal())

            if (self.goal_angle2 < 40):
                reward += 5

        return reward

    def get_state(self, index):
        l = list()
        self.fail = False
        self.success = False
        l.append(self.get_abs_distance_to_goal(index))
        l.append(float(self.min_ldss_dist[index]))
        l.append(float(self.goal_angles[index]))
        


        if (self.crashs(index)):
                print(f"get reward of -10 {id}")
                self.fail = True
                self.done = True
                self.steps = 0
                self.call_reset_sim()
               

        if (self.goal_reached(index)):
                self.stop_robots(index)
                self.succeses[index] = True
                self.done = True
                self.steps = 0
                req = Empty.Request()
                while not self.reset_sim_client.wait_for_service(timeout_sec=1.0):
                    self.get_logger().info('service not available, waiting again...')

                self.reset_sim_client.call_async(req)

        if (self.steps == 500):
                self.done = True
                self.fail = True
                self.steps = 0
                req = Empty.Request()
                while not self.reset_sim_client.wait_for_service(timeout_sec=1.0):
                    self.get_logger().info('service not available, waiting again...')

                self.reset_sim_client.call_async(req)
            self.steps += 1
            return l
    
        else:
            l.append(self.get_distance_to_goal(self.goal_cord2, 2))
            l.append(float(self.min_lds_dist2))
            l.append(float(self.goal_angle2))
            return l


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
