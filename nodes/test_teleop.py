#!/usr/bin/env python
import rospy
import sys
import math
import tf
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

wall_ahead = False

# fill in scan callback
def scan_cb(msg):
   global ahead
   ahead = msg.ranges[0]
   if ahead <= 2:
      wall_ahead = True
   else:
      wall_ahead = False

ahead = 5

# it is not necessary to add more code here but it could be useful
def key_cb(msg):
   global state; global last_key_press_time
   state = msg.data
   last_key_press_time = rospy.Time.now()

# odom is also not necessary but very useful
def odom_cb(msg):
   global pose
   pose = msg.pose
   return

pose = None
global speed
speed = 0

# print the state of the robot
def print_state():

   # Looks 9000% better than print spam
   for i in range (0,30):
         print()
   
   print("---")
   print("STATE: " + state)

   # calculate time since last key stroke
   time_since = rospy.Time.now() - last_key_press_time
   print("SECS SINCE LAST KEY PRESS: " + str(time_since.secs))

def get_time_since():
   return rospy.Time.now() - last_key_press_time

# init node
rospy.init_node('dancer')

# subscribers/publishers
scan_sub = rospy.Subscriber('scan', LaserScan, scan_cb)

# RUN rosrun prrexamples key_publisher.py to get /keys
key_sub = rospy.Subscriber('keys', String, key_cb)
odom_sub = rospy.Subscriber('odom', Odometry, odom_cb)

r1_cmd_vel_pub = rospy.Publisher('robot1/cmd_vel', Twist, queue_size=10)
r2_cmd_vel_pub = rospy.Publisher('robot2/cmd_vel', Twist, queue_size=10)

# start in state halted and grab the current time
state = "h"
last_key_press_time = rospy.Time.now()

# set rate
rate = rospy.Rate(10)

def get_components(char):
   vectors = {'h': [0,0], 's': [1,1], 'z': [1,0], 
   'w': [1,0], 'a': [0,1], 's': [-1,0], 'd':[0,-1], ' ':[0,0],
   'i': [10,0], 'j': [0,.8], 'k': [-5,0], 'l':[0,-.5], ' ':[0,0]}
   return vectors[char]

# Wait for published topics, exit on ^c
while not rospy.is_shutdown():

   print_state()
   t = Twist()

   component_vector = get_components(state)

   linear_component = component_vector[0]
   angular_component = component_vector[1]

   linear_speed = .5
   angular_speed = 1

   t.linear.x = linear_speed * linear_component
   t.angular.z = angular_speed * angular_component

   # change Twist linear speed over time for spiral movement
   if state == 's':
      # Spiral goes "inward"
      time_since_int = get_time_since().secs
      t.linear.x = t.linear.x - (.1 * time_since_int)
      if (t.linear.x <= -1):
         state = 'h'


   # change Twist at certain interval for zigzag movement
   if state == 'z':
      time_since_int = get_time_since().secs

      started_zagging = False
      finished_zagging = False

      # stop and change direction every 6 seconds
      # Stopping is for 2 seconds
      if ((time_since_int % 6 == 0 or time_since_int % 6 == 1) and (time_since_int != 0 or time_since_int != 1)):
         started_zagging = True
         t.linear.x = 0

         # So we will alternate between going left or right, every other 6-second cycle
         if (time_since_int % 12 == 0 or time_since_int % 12 == 1):
            t.angular.z = 1
         else:
            t.angular.z = -1


   speed = t.linear.x

   # =========================

   r1_cmd_vel_pub.publish(t)
   r2_cmd_vel_pub.publish(t)

   # run at 10hz
   rate.sleep()
