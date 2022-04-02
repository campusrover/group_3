#!/usr/bin/env python  
import rospy

import math
import tf2_ros
import geometry_msgs.msg
import geometry_msgs/Transform.msg
import turtlesim.srv

from nav_msgs.msg import Odometry

if __name__ == '__main__':
    rospy.init_node('listener')

    r1_pos = geometry_msgs.msg
   
    r2_coords = []

    def odom_cb_1(msg):
        global r1_coords
        r1_coords = []
        r1_coords.append(msg.pose.pose.position.x)
        r1_coords.append(msg.pose.pose.position.y)
        r1_coords.append(msg.pose.pose.position.z)

    def odom_cb_2(msg):
        global r2_coords
        r2_coords = []
        r2_coords.append(msg.pose.pose.position.x)
        r2_coords.append(msg.pose.pose.position.y)
        r2_coords.append(msg.pose.pose.position.z)


    # cmdvel_1 = rospy.Publisher('robot1/cmd_vel', geometry_msgs.msg.Twist, queue_size=1)
    cmdvel_2 = rospy.Publisher('robot2/cmd_vel', geometry_msgs.msg.Twist, queue_size=1)

    odom_sub_1 = rospy.Subscriber('robot1/odom',Odometry,odom_cb_1)
    odom_sub_2 = rospy.Subscriber('robot2/odom',Odometry,odom_cb_2)

    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        msg = geometry_msgs.msg.Twist()

        # msg.angular.z = 4 * math.atan2(trans.transform.translation.y, trans.transform.translation.x)
        # msg.linear.x = 0.5 * math.sqrt(trans.transform.translation.x ** 2 + trans.transform.translation.y ** 2)

        tf1 = geometry_msgs.msg.TransformStamped()

        t.transform.translation.x = r1_coords[0]
        t.transform.translation.y = r1_coords[1]
        t.transform.translation.z = r1_coords[2]

        # print(r1_coords)
        # print(r2_coords)

        # cmdvel_2.publish(msg)

        rate.sleep()