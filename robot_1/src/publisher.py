#! /usr/bin/env python
import rospy
from std_msgs.msg import Float64

rospy.init_node('publisher')
pub1 = rospy.Publisher('/robot_1/rear_left_controller/command', Float64, queue_size=10)
pub2 = rospy.Publisher('/robot_1/rear_left_controller/command', Float64, queue_size=10)
rate = rospy.Rate(2)
speed = -50.0

while not rospy.is_shutdown():
    pub1.publish(-speed)
    pub2.publish(speed)
    rospy.loginfo('Moving with velocity {}'.format(speed))
    rate.sleep()

    