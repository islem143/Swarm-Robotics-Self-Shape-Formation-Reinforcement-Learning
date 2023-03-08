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


class Env(Node):

    def __init__(self):
        super().__init__('env')
        self.get_odom = self.create_subscription(
            Odometry, "/t1/odom", self.get_current_position, 10)
        self.get_laser = self.create_subscription(
            LaserScan, "/t1/scan", self.get_lds, 10)
        self.cmd_vel_pub = self.create_publisher(Twist, '/t1/cmd_vel', 10)
       # self.publish_state=self.create_publisher(State, "/state", 10)
       # self.create_timer(3, self.step)
        self.env_result_service = self.create_service(
            Dqnn, "env_result", self.step)
        self.env_goal_service = self.create_service(
            Goal, "goal_pose", self.generate_goal_pose)
        self.reset_sim_client = self.create_client(Empty, "reset_sim")
       # self.stop_robot()

    def get_current_position(self, msg):

        self.position_x = msg.pose.pose.position.x
        self.position_y = msg.pose.pose.position.y
        self.angle = self.euler_from_quaternion(msg.pose.pose.orientation)[2]
        self.goal_angle = np.abs(
            self.angle-np.arctan2(np.abs(self.position_y-0.1), np.abs(self.position_x-0.1)))
        print(self.goal_angle)
    def get_lds(self, msg):

        self.min_lds_dist = np.min(msg.ranges)
        if(self.min_lds_dist==np.Inf):
            self.min_lds_dist=float(4)
       #self.min_lds_angle = np.argmin(msg.ranges)

    def init_robot(self):

        twist = Twist()
        twist.linear.x = 0.3
        self.cmd_vel_pub.publish(twist)

    def move_robot(self, action):
        twist = Twist()
        twist.linear.x = 0.3
        twist.angular.z = action
        self.cmd_vel_pub.publish(twist)

    def stop_robot(self):
        self.cmd_vel_pub.publish(Twist())

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
        req = Empty.Request()
        while not self.reset_sim_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.reset_sim_client.call_async(req)

    def step(self, request, response):
        if (request.init):
            self.init_robot()

        actions_index = request.action

        actions = [-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2]
        action = float(actions[actions_index])
        done = False
        self.move_robot(action)

        if (self.crash()):
            print("crash")
            self.call_reset_sim()
            done = True
        if (self.goal_reached()):

            self.call_reset_sim()
            done = True
        state_s = self.get_state()
        reward = self.get_reward()

        response.state = state_s
        response.reward = reward
        response.done = done
        return response

    def get_distance_to_goal(self):
        return float(np.sqrt(np.square(self.position_y-0.1)+np.square(self.position_x-0.1)))

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

    def goal_reached(self):
        distance = self.get_distance_to_goal()
        if (distance < 0.20):
            print("gooooooal")
            return True
        return False

    def get_reward(self):

        distance = self.get_distance_to_goal()
        reward = 10*(1/distance)
        reward += 2*(1/self.goal_angle)
        # if(self.goal_angle<0.15):
        #     reward+=10
        #     print("yessssssss")
        if (self.crash()):
            print("get reward of -10")
            reward -= 10
        if (self.goal_reached()):
            print("get reward of +200")
            reward += 200
        # else:
        #     reward-=1
        print("reward", reward)
        return reward

    def get_state(self):
        l = list()
        l.append(self.get_distance_to_goal())
        l.append(float(self.min_lds_dist))
        l.append(float(self.goal_angle))
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
