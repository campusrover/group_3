#!/usr/bin/env python  
import turtle
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose

import turtlesim.msg

class PosePub:

    def __init__(self, turtlename):
        self.pub = rospy.Publisher(f"{turtlename}/pose",Pose, queue_size=1)
        self.sub = rospy.Subscriber(f"{turtlename}/odom",Odometry,self.handle_turtle_pose)

    def handle_turtle_pose(self, msg: Odometry):
        turtle_pose = msg.pose.pose
        self.pub.publish(turtle_pose)

        br = tf2_ros.TransformBroadcaster()
        t = geometry_msgs.msg.TransformStamped()
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = f"{turtlename}/odom"
        t.child_frame_id = turtlename
        t.transform.translation.x = msg.pose.pose.position.x
        t.transform.translation.y = msg.pose.pose.position.y
        t.transform.translation.z = 0.0
        t.transform.rotation.x = msg.pose.pose.orientation.x
        t.transform.rotation.y = msg.pose.pose.orientation.y
        t.transform.rotation.z = msg.pose.pose.orientation.z
        t.transform.rotation.w = msg.pose.pose.orientation.w

        br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('broadcaster')
    turtlename = rospy.get_param('~turtle')
    pub = PosePub(turtlename)
    rospy.spin()