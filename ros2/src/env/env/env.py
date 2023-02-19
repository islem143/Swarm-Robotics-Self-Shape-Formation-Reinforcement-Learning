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

from dqn_msg.msg import State


class Env(Node):
     

    def __init__(self):
        super().__init__('env')
        self.get_odom=self.create_subscription(Odometry, "/t1/odom", self.get_current_position,10)
        self.get_laser=self.create_subscription(LaserScan, "/t1/scan", self.get_lds,10)
        self.cmd_vel_pub = self.create_publisher(Twist, '/t1/cmd_vel', 10)
        self.publish_state=self.create_publisher(State, "/state", 10)
        self.create_timer(3, self.step)
        #self.stop_robot()
    


    def get_current_position(self,msg):
    
        self.position_x=msg.pose.pose.position.x
        self.position_y=msg.pose.pose.position.y
        self.angle=self.euler_from_quaternion(msg.pose.pose.orientation)[2]
       
    def get_lds(self,msg):
        self.min_lds_dist=np.min(msg.ranges)
        self.min_lds_angle=np.argmin(msg.ranges)    

    def init_robot(self):

         twist=Twist()
         twist.linear.x=0.5
         self.cmd_vel_pub.publish(twist) 

    def move_robot(self,action):
        twist=Twist()
        twist.linear.x=0.5
        twist.angular.z=action
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

   
    def step(self):
        state=State()
        
        actions_index=np.random.randint(0,4)
            
        actions=[-np.pi/2,-np.pi/4,0,np.pi/4,np.pi/2]
        action=float(actions[actions_index])
       
        #self.move_robot(action)
        state_s=self.get_state()
        reward=self.get_reward()
        done=False
        state.state=state_s
        state.reward=reward
        state.done=done
        self.publish_state.publish(state)    


    def action():
        pass
    def get_reward(self):
        distance=np.sqrt(np.square(self.position_y-0.0)+np.square(self.position_x-0.0))
        reward=(-distance)**2
        return reward
    def get_state(self):
        l=list()
        l.append(self.position_x)
        l.append(self.position_y)
        l.append(float(self.min_lds_dist))
        l.append(float(self.min_lds_angle))
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



     
