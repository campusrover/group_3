#!/usr/bin/env python
import rospy
import actionlib

import geometry_msgs.msg
import geometry_msgs
import move_base_msgs
import std_msgs

# move_base is the package that takes goals for navigation
# there are different implemenetations with a common interface
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


class Mover:
    def __init__(self, turtlename):
        self.pub = rospy.Publisher(f"{turtlename}/pose", Pose, queue_size=1)
        self.sub = rospy.Subscriber(f"{turtlename}/odom",Odometry,self.handle_turtle_pose)
        self.sub = rospy.Subscriber(f"{turtlename}/odom",Odometry,self.handle_turtle_pose)

    def handle_turtle_pose(self, msg):
        turtle_pose = msg.pose.pose
        self.pub.publish(turtle_pose)

    # This is called by other programs, I am planning
    # subscribe to 
    
    # th
        



if __name__ == '__main__':
    rospy.init_node('mover')
    turtlename = rospy.get_param('~name')
    pub = PosePub(turtlename)

    

    rospy.spin()


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