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
from dqn_msg.msg import Goal
import time


class Env(Node):

    def __init__(self):
        super().__init__('env')
        self.get_odom = self.create_subscription(
            Odometry, "/t1/odom", self.get_current_position, 10)
        self.get_laser = self.create_subscription(
            LaserScan, "/t1/scan", self.get_lds, 10)
        self.cmd_vel_pub = self.create_publisher(Twist, '/t1/cmd_vel', 10)
        self.get_odom2 = self.create_subscription(
            Odometry, "/t2/odom", self.get_current_position2, 10)
        self.get_laser2 = self.create_subscription(
            LaserScan, "/t2/scan", self.get_lds2, 10)
        self.cmd_vel_pub2 = self.create_publisher(Twist, '/t2/cmd_vel', 10)

        self.env_result_service = self.create_service(
            Dqnn, "env_result", self.step)
        # self.env_goal_service = self.create_service(
        #     Goal, "goal_pose", self.generate_goal_pose)
        self.reset_sim_client = self.create_client(Empty, "reset_sim")
        self.goal_cord = [0.0, 0.0]
        self.goal_cord2 = [0.01, 0.01-1]
        self.done = False
        self.goal_publisher=self.create_publisher(Goal,"generate_goal",10)
        self.steps = 0
        self.position_x = 0

        self.position_y = 0
        self.position_x2 = 0
        self.position_y2 = 0
        self.angle = 0
        self.angle2 = 0
        self.goal_angle = 0
        self.goal_angle2 = 0
        self.init_position = [-1.5, 1.2]
        
       # self.stop_robot()

    # def check(self):
    #     if (self.done):
    #         time.sleep(2)
    #         self.call_reset_sim()
    #         self.done = False

    def get_current_position(self, msg):

        self.position_x = msg.pose.pose.position.x
        self.position_y = msg.pose.pose.position.y
        self.angle = self.euler_from_quaternion(msg.pose.pose.orientation)[2]
        self.goal_angle = self.get_goal_angle(self.goal_cord)
        
        
       

    def get_current_position2(self, msg):
        self.position_x2 = msg.pose.pose.position.x
        self.position_y2 = msg.pose.pose.position.y
        self.angle2 = self.euler_from_quaternion(msg.pose.pose.orientation)[2]
        self.goal_angle2 = self.get_goal_angle2(
            self.goal_cord2)

    def get_lds(self, msg):

        self.min_lds_dist = np.min(msg.ranges)

        if (self.min_lds_dist == np.Inf):
            self.min_lds_dist = float(4)
       #self.min_lds_angle = np.argmin(msg.ranges)

    def get_lds2(self, msg):

        self.min_lds_dist2 = np.min(msg.ranges)
        if (self.min_lds_dist2 == np.Inf):
            self.min_lds_dist2 = float(4)

    def get_goal_angle(self, goal):
        if (self.position_x > goal[0] and self.position_y > goal[1]):

            return np.abs(self.angle-(np.arctan2(np.abs(self.position_y-goal[1]), np.abs(self.position_x-goal[0]))-np.pi))
        elif (self.position_x < goal[0] and self.position_y < goal[1]):
            return np.abs(self.angle-(np.arctan2(np.abs(self.position_y-goal[1]), np.abs(self.position_x-goal[0]))))
        elif (self.position_x > goal[0] and self.position_y < goal[1]):
            return np.abs(self.angle-(np.arctan2(np.abs(self.position_x-goal[0]), np.abs(self.position_y-goal[1]))+np.pi/2))
        else:
            return np.abs(self.angle-(np.arctan2(np.abs(self.position_x-goal[0]), np.abs(self.position_y-goal[1]))-np.pi/2))

    def get_goal_angle2(self, goal):
        if (self.position_x2 > goal[0] and self.position_y2 > goal[1]):

            return np.abs(self.angle2-(np.arctan2(np.abs(self.position_y2-goal[1]), np.abs(self.position_x2-goal[0]))-np.pi))
        elif (self.position_x2 < goal[0] and self.position_y2 < goal[1]):
            return np.abs(self.angle2-(np.arctan2(np.abs(self.position_y2-goal[1]), np.abs(self.position_x2-goal[0]))))
        elif (self.position_x2 > goal[0] and self.position_y2 < goal[1]):
            return np.abs(self.angle2-(np.arctan2(np.abs(self.position_x2-goal[0]), np.abs(self.position_y2-goal[1]))+np.pi/2))
        else:
            return np.abs(self.angle2-(np.arctan2(np.abs(self.position_x2-goal[0]), np.abs(self.position_y2-goal[1]))-np.pi/2))

    def init_robot(self):

        twist = Twist()
        twist.linear.x = 0.3

        self.cmd_vel_pub.publish(twist)

    def init_robot2(self):

        twist = Twist()
        twist.linear.x = 0.3
        self.cmd_vel_pub2.publish(twist)

    def move_robot(self, action):
        twist = Twist()
        twist.linear.x = 0.3
        twist.angular.z = action
        self.cmd_vel_pub.publish(twist)

    def move_robot2(self, action):
        twist = Twist()
        twist.linear.x = 0.3
        twist.angular.z = action
        self.cmd_vel_pub2.publish(twist)

    def stop_robot(self):
        self.cmd_vel_pub.publish(Twist())
        self.stop = True

    def stop_robot2(self):
        self.stop2 = True
        self.cmd_vel_pub2.publish(Twist())

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
        self.stop_robot()
        self.stop_robot2()
       
        req = Empty.Request()
        while not self.reset_sim_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.reset_sim_client.call_async(req)

    def get_abs_distance_to_goal(self):
        return float(np.sqrt(np.square(self.init_position[1]-self.goal_cord[1])+np.square(self.init_position[0]-self.goal_cord[0])))

    def step(self, request, response):
        if (request.init):
            response.state = self.get_state(1)
            self.init_position = [self.position_x, self.position_y]

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

    def get_distance_to_goal(self, goal, id):
        if (id == 1):
            return float(np.sqrt(np.square(self.position_y-goal[1])+np.square(self.position_x-goal[0])))
        else:
            return float(np.sqrt(np.square(self.position_y2-goal[1])+np.square(self.position_x2-goal[0])))

    def generate_goal_pose(self):
        x = float(np.random.randint(-2.5, 2.5))
        y = float(np.random.randint(-2.5, 2.5))
        self.goal_cord[0]=x
        self.goal_cord[1]=y
        x = float(np.random.randint(-2.5, 2.5))
        y = float(np.random.randint(-2.5, 2.5))
        self.goal_cord2[0]=x
        self.goal_cord2[1]=y
        msg = Goal()                                               
        msg.goal = [x,y]                                          
        self.goal_publisher.publish(msg)
        
        

    def crash(self):
        if (self.min_lds_dist < 0.13):

            return True
        return False

    def crash2(self):
        if (self.min_lds_dist2 < 0.25):

            return True
        return False

    def goal_reached(self):

        distance = self.get_distance_to_goal(self.goal_cord, 1)
        distance2 = self.get_distance_to_goal(self.goal_cord2, 2)
        if (distance < 0.20 and distance2 < 0.20):
            print("gooooooal")
            self.stop_robot()
            self.stop_robot2()
            return True
        return False

    def goal_reached_local(self, goal, id):
        distance = self.get_distance_to_goal(goal, id)

        if (distance < 0.20):
            #print(f"gooooooal {id}")

            return True
        return False
   # def angle_to_goal(self):
        # if(self.position_x>0.01 and self.position_y>0.01 and )

    def get_reward(self, id):
        reward = 0.0
        if (id == 1):
            distance=self.get_distance_to_goal(self.goal_cord,1)
            reward+=-(distance/self.get_abs_distance_to_goal())

            
            
            if (self.goal_angle < 0.40):
                reward += 5
            print(reward)
            
                  
            if self.success:
                reward += 100
            elif self.fail:
                reward -= 100

        else:
            distance=self.get_distance_to_goal(self.goal_cord2,2)
            reward+=-(distance/self.get_abs_distance_to_goal())

            if (self.goal_angle2 < 40):
                reward += 5

             

        return reward

    def get_state(self, id):
        l = list()
        self.fail = False
        self.success = False
        print(self.goal_cord)

        if (id == 1):

            l.append(self.get_distance_to_goal(self.goal_cord, 1))
            l.append(float(self.min_lds_dist))
            l.append(float(self.goal_angle))
            

            if (self.crash()):
                print(f"get reward of -10 {id}")
                self.fail = True
                self.done = True
                self.steps = 0
                req = Empty.Request()
                while not self.reset_sim_client.wait_for_service(timeout_sec=1.0):
                    self.get_logger().info('service not available, waiting again...')

                self.reset_sim_client.call_async(req)

            if (self.goal_reached_local(self.goal_cord, 1)):
                self.stop_robot()

                self.success = True
                self.done = True
                self.steps = 0
                req = Empty.Request()
                while not self.reset_sim_client.wait_for_service(timeout_sec=1.0):
                    self.get_logger().info('service not available, waiting again...')

                self.reset_sim_client.call_async(req)
                self.generate_goal_pose()

            # if (self.steps == 500):
            #     self.done = True
            #     self.fail = True
            #     self.steps = 0
            #     req = Empty.Request()
            #     while not self.reset_sim_client.wait_for_service(timeout_sec=1.0):
            #         self.get_logger().info('service not available, waiting again...')

            #     self.reset_sim_client.call_async(req)
            self.steps += 1
            return l
        else:
            l.append(self.get_distance_to_goal(self.goal_cord2,2))
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
