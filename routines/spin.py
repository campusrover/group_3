import rospy
import time
from geometry_msgs.msg import Twist

#Description:
#Makes the robot spin in place

##Creating Variables
global speed
###Callback Fxns
def key_cb(msg):
   global state
   global last_key_press_time
   state = msg.data
   last_key_press_time = rospy.Time.now()
def odom_cb(msg):
   global pose
   pose = msg.pose
   return
###Setting Initial Values
pose = None
speed = 0

def gui():
    for i in range(0,10):
        print()
    print("=======")
    