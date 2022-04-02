#!/usr/bin/env python  
import rospy

import math
import tf2_ros
import geometry_msgs.msg
import geometry_msgs
import move_base_msgs
import std_msgs
import turtlesim.srv

from move_base_msgs.msg import MoveBaseGoal

if __name__ == '__main__':
    rospy.init_node('listener')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    turtle_name = rospy.get_param('turtle','robc')
    #mode = rospy.get_param('mode')

    #Velocity publishers
    turtle_vel = rospy.Publisher('%s/cmd_vel' % turtle_name, geometry_msgs.msg.Twist, queue_size=1)
    #turtle_goal = rospy.Publisher('%s/move_base/goal' % turtle_name, geometry_msgs.msg.Twist, queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        
        mbg = MoveBaseGoal()
        print(mbg.target_pose.header)


        try:
            trans = tfBuffer.lookup_transform(turtle_name, 'rafael', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        msg = geometry_msgs.msg.Twist()

        y=trans.transform.translation.y
        if(y<0.5):
            y=0
        x=trans.transform.translation.x
        if(x<0.5):
            x=0

        msg.angular.z = 0.10 * math.atan2(y, x)
        msg.linear.x = 0.25 * math.sqrt(x**2 + y**2)

        # if mode == 'manual':
        #     turtle_vel.publish(msg)
        
        # if mode == 'move_base': 
        #     msg = move_base_msgs.MoveBaseGoal.msg
        #     header = std_msgs.header
        #     header.seq = 1 

        #     turtle_goal.publish()

        turtle_vel.publish(msg)

        rate.sleep()


# THIS IS WHAT A MOVE BASE MSG LOOKS LIKE
# header: 
#   seq: 1
#   stamp: 
#     secs: 3722
#     nsecs: 997000000
#   frame_id: ''
# goal_id: 
#   stamp: 
#     secs: 0
#     nsecs:         0
#   id: ''
# goal: 
#   target_pose: 
#     header: 
#       seq: 7
#       stamp: 
#         secs: 3722
#         nsecs: 997000000
#       frame_id: "odom"
#     pose: 
#       position: 
#         x: 2.505542278289795
#         y: -1.008162498474121
#         z: 0.0
#       orientation: 
#         x: 0.0
#         y: 0.0
#         z: -0.5817760734820274
#         w: 0.8133490027803776
