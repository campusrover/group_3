#!/usr/bin/env python  
import rospy

import math
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('listener')


    # cmdvel_1 = rospy.Publisher('robot1/cmd_vel', geometry_msgs.msg.Twist, queue_size=1)
    cmdvel_2 = rospy.Publisher('robot2/cmd_vel', geometry_msgs.msg.Twist, queue_size=1)

    rate = rospy.Rate(10.0)

    r1_pos = (0,0,0)

    def odom_cb(msg):
        global r1_pos
        r1_pos = msg.pose.pose.position
        print(r1_pos)

    while not rospy.is_shutdown():

        # trans = r1_pos

        # msg = geometry_msgs.msg.Twist()

        # msg.angular.z = 4 * math.atan2(trans.transform.translation.y, trans.transform.translation.x)
        # msg.linear.x = 0.5 * math.sqrt(trans.transform.translation.x ** 2 + trans.transform.translation.y ** 2)

        # turtle_vel.publish(msg)

        rate.sleep()