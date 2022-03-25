#!/usr/bin/env python  
import rospy

import math
import tf2_ros
import geometry_msgs.msg
from geometry_msgs.msg import Twist
# import geometry_msgs/Transform.msg
import turtlesim.srv

from nav_msgs.msg import Odometry


if __name__ == '__main__':
    rospy.init_node('square')


    waypoints = [[1,0],[0,0]]

    r1_odom = None

    def odom_cb(msg):
        global r1_odom
        r1_odom = msg

    odom_sub = rospy.Subscriber('rafael/odom',Odometry,odom_cb)
    cmdvel = rospy.Publisher('rafael/cmd_vel', geometry_msgs.msg.Twist, queue_size=1)


    while not rospy.is_shutdown():
        print(r1_odom)

        if (r1_odom != None):
            while (r1_odom.pose.pose.position.x < 1):
                twist = Twist()
                twist.linear.x = .2
                cmdvel.publish()
                
            rospy.spin()    

