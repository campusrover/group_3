#!/usr/bin/env python
import rospy
import actionlib

# move_base is the package that takes goals for navigation
# there are different implemenetations with a common interface
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal




# Main program starts here
if __name__ == '__main__':

    # A node called 'patrol' which is an action client to move_base
    rospy.init_node('patrol')
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    # wait for action server to be ready
    client.wait_for_server()

    # Loop until ^c
    while not rospy.is_shutdown():

