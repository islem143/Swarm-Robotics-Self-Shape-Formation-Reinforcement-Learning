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

action_map = {}
for i in range(25):
    # Change i to base 5 (possible actions)
    action = [0] * 2
    num = i
    index = -1
    while num > 0:
        action[index] = num % 5
        num = num // 5
        index -= 1
    action_map[i] = action


class Env(Node):

    def __init__(self):
        super().__init__('env')
        self.angle = 0
        self.position_x = 0
        self.position_y = 0
        self.angle2 = 0
        self.position_x2 = 0
        self.position_y2 = 0
        self.get_odom1 = self.create_subscription(
            Odometry, "/t1/odom", self.get_current_position, 10)
        self.get_laser1 = self.create_subscription(
            LaserScan, "/t1/scan", self.get_lds, 10)
        self.cmd_vel_pub1 = self.create_publisher(Twist, '/t1/cmd_vel', 10)

        self.get_odom2 = self.create_subscription(
            Odometry, "/t2/odom", self.get_current_position2, 10)
        self.get_laser2 = self.create_subscription(
            LaserScan, "/t2/scan", self.get_lds2, 10)
        self.cmd_vel_pub2 = self.create_publisher(Twist, '/t2/cmd_vel', 10)

        self.env_result_service = self.create_service(
            Dqnn, "env_result", self.step)
        self.env_goal_service = self.create_service(
            Goal, "goal_pose", self.generate_goal_pose)
        self.reset_sim_client = self.create_client(Empty, "reset_sim")
        self.angle = 0
        self.position_x = 0
        self.position_y = 0
        self.angle2 = 0
        self.position_x2 = 0
        self.position_y2 = 0
        self.r1_goal = False
        self.r2_goal = False
        self.min_lds_dist = 5
        self.min_lds_dist2 = 0

       # self.stop_robot()

    def get_current_position(self, msg):

        self.position_x = msg.pose.pose.position.x
        self.position_y = msg.pose.pose.position.y
        self.angle = self.euler_from_quaternion(msg.pose.pose.orientation)[2]
        self.goal_angle = np.abs(
            self.angle-np.arctan2(np.abs(self.position_y2-1.5), np.abs(self.position_x2-1.5)))

    def get_current_position2(self, msg):

        self.position_x2 = msg.pose.pose.position.x
        self.position_y2 = msg.pose.pose.position.y
        self.angle2 = self.euler_from_quaternion(msg.pose.pose.orientation)[2]
        self.goal_angle2 = np.abs(
            self.angle-np.arctan2(np.abs(self.position_y2-1.5), np.abs(self.position_x2-1.5)))

    def get_lds2(self, msg):

        self.min_lds_dist2 = np.min(msg.ranges)
        if (self.min_lds_dist2 == np.Inf):
            self.min_lds_dist2 = float(4)
        print("lds 1", self.min_lds_dist2)

    def get_lds(self, msg):

        self.min_lds_dist = np.min(msg.ranges)
        if (self.min_lds_dist == np.Inf):
            self.min_lds_dist = float(4)
        print("lds2", self.min_lds_dist)
       #self.min_lds_angle = np.argmin(msg.ranges)

    def init_robot(self):

        twist = Twist()
        twist.linear.x = 0.3
        self.cmd_vel_pub1.publish(twist)

    def init_robot2(self):

        twist = Twist()
        twist.linear.x = 0.3
        self.cmd_vel_pub2.publish(twist)

    def move_robot1(self, action):
        twist = Twist()
        twist.linear.x = 0.3
        twist.angular.z = action
        self.cmd_vel_pub1.publish(twist)

    def move_robot2(self, action):
        twist = Twist()
        twist.linear.x = 0.3
        twist.angular.z = action
        self.cmd_vel_pub2.publish(twist)

    def stop_robot(self):
        self.cmd_vel_pub1.publish(Twist())

    def stop_robot2(self):
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
        self.r1_goal = False
        self.r2_goal = False
        self.stop_robot()
        self.stop_robot2()
        req = Empty.Request()
        while not self.reset_sim_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.reset_sim_client.call_async(req)

    def step(self, request, response):

        if (request.init):
            self.init_robot()
            self.init_robot2()

        actions_index = request.action

        actions = [-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2]
        action_r1 = action_map[actions_index][0]
        action_r2 = action_map[actions_index][1]
        action_r1 = float(actions[action_r1])
        action_r2 = float(actions[action_r2])
        done = False
        done2= False

        self.move_robot1(action_r1)
        self.move_robot2(action_r2)

        if (self.crash() or self.crash2()):
            print("crash")
            self.call_reset_sim()
            done = True
        if (self.goal_reached()):

            self.stop_robot()
            done = True
        if (self.goal_reached2()):

            self.stop_robot2()
            done2 = True    
        state_s = self.get_state()
        reward = self.get_reward()

        response.state = state_s
        response.reward = reward
        response.done = [done,done2]
        return response

    def get_distance_to_goal(self):
        return float(np.sqrt(np.square(self.position_y-0.1)+np.square(self.position_x-0.1)))

    def get_distance_to_goal2(self):
        return float(np.sqrt(np.square(self.position_y2-0.1)+np.square(self.position_x2-0.1)))

    def generate_goal_pose(self):
        x = float(np.random.randint(-4, 4))
        y = float(np.random.randint(-4, 4))
        self.goal_x = x
        self.goal_y = y
        return x, y

    def crash(self):
        if (self.min_lds_dist < 0.25):

            return True
        return False

    def crash2(self):
        if (self.min_lds_dist2 < 0.25):

            return True
        return False

    def goal_reached(self):
        if (self.min_lds_dist > 0.95 and self.min_lds_dist < 1.05 and self.get_distance_to_goal() < 2):
            print("goal reached 1")
            return True
        return False
    def goal_reached2(self):
        if (self.min_lds_dist2 > 0.95 and self.min_lds_dist2 < 1.05 and self.get_distance_to_goal2() < 2):
            print("goal  reached 2")
            return True
        return False

         
    def get_reward(self):
        reward_r1 = 0
        reward_r2 = 0

        distance1 = self.get_distance_to_goal()
        distance2 = self.get_distance_to_goal2()
        angle1 += 2*(1/self.goal_angle)
        angle2 += 2*(1/self.goal_angle2)
        reward_r1 += 2*(1/distance1)
        reward_r2 += 2*(1/distance2)
        reward_r1+=angle1
        reward_r2+=angle2
        
        if (self.crash()):
            reward_r1 -= 10
        if (self.crash2()):
            reward_r2 -= 10
        if (self.goal_reached):
            reward_r1 += 100
           
        if (self.goal_reached2):
            reward_r2 += 100


        
        return [reward_r1,reward_r2]

    def get_state(self):
        l = list()
        l.append([self.get_distance_to_goal(), float(
            self.min_lds_dist), float(self.goal_angle)])
        l.append([self.get_distance_to_goal2(), float(
            self.min_lds_dist2), float(self.goal_angle2)])

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
