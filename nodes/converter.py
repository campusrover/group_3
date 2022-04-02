#!/usr/bin/env python  
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg
import turtlesim.msg


# What does this do?

# This is to cpublish a tf that is uh, the conversion between robc/base_footprint and rafael/base_footprint
# These can be chained I think, so convert one to the other by ... something...
# this is a good place to use a tutorial. so I need to find the differene between the two and publish that as a tf?
# ... uh... uh...

def handle_turtle_pose(msg, turtlename):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "world"
    t.child_frame_id = turtlename
    t.transform.translation.x = msg.x
    t.transform.translation.y = msg.y
    t.transform.translation.z = 0.0
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('broadcaster')
    # turtlename = rospy.get_param('~turtle') #<--- need to figure out param name change
    # rospy.Subscriber('/%s/pose' % turtlename,turtlesim.msg.Pose,handle_turtle_pose,turtlename)
    rospy.Subscriber('/rafael/pose',turtlesim.msg.Pose,handle_turtle_pose,'rafael')
    rospy.spin()