#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as Np
def callback(msg):
	
 	print('s1 [270]')
	print msg.ranges[270]
	print('s2 [0]')
	print msg.ranges[0]
	print('s3 [90]')
	print msg.ranges[90]
	
	if msg.ranges[0]>0.6:
		move.linear.x=0.2
		move.angular.z=0.0
	else:
         	move.linear.x=0.0
		move.angular.z=0.5
    	pub.publish(move)

rospy.init_node('obstacle_avoidance')
sub=rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist)
move=Twist()
rospy.spin()


