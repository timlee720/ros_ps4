#! /usr/bin/python

'''
Usage:
# Publish the msg to ROS serial
'''

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

class Talker:
    def __init__(self):
        # ROS topics
        self.manual_pub = rospy.Publisher('omni_drive_control/cmd_vel', Twist, queue_size=10)     # manual mode
        self.auto_pub = rospy.Publisher('/auto_topic', Twist, queue_size=10)    # auto mode

        self.cross_pub = rospy.Publisher('/cross_topic', Bool, queue_size = 10)    # cross button
        self.circle_pub = rospy.Publisher('/circle_topic', Bool, queue_size = 10)   # circle button
        self.tri_pub = rospy.Publisher('/tri_topic', Bool, queue_size = 10)     # triangle button
        self.sqaure_pub = rospy.Publisher('/square_topic', Bool, queue_size = 10)    # square button

        self.share_pub = rospy.Publisher('/share_topic', Bool, queue_size = 10)   # share button
        self.option_pub = rospy.Publisher('/option_topic', Bool, queue_size = 10)     # option button
        self.ps_pub = rospy.Publisher('/ps_topic', Bool, queue_size = 10)   # playstation button

        self.r1_pub = rospy.Publisher('/r1_topic', Bool, queue_size = 10)     # R1 button
        self.l1_pub = rospy.Publisher('/l1_topic', Bool, queue_size = 10)    # L1 button

    #---------------------------------------------------------
    # ROS publish

    # Manual input all velocity 
    def manualPublish(self, vel_msg):
        rospy.loginfo(vel_msg)
        self.manual_pub.publish(vel_msg)
        return
    
    # Auto input linear, manual input angular
    def autoPublish(self, vel_msg):
        rospy.loginfo(vel_msg)
        self.auto_pub.publish(vel_msg)
        return

    # Buttons
    def crossPublish(self, state):
        # rospy.loginfo(state)
        self.cross_pub.publish(state)
        return

    def circlePublish(self, state):
        # rospy.loginfo(state)
        self.circle_pub.publish(state)
        return
        
    def triPublish(self, state):
        # rospy.loginfo(state)
        self.tri_pub.publish(state)
        return
        
    def squarePublish(self, state):
        # rospy.loginfo(state)
        self.sqaure_pub.publish(state)
        return
        
    def sharePublish(self, state):
        # rospy.loginfo(state)
        self.share_pub.publish(state)
        return
        
    def optionPublish(self, state):
        # rospy.loginfo(state)
        self.option_pub.publish(state)
        return
        
    def psPublish(self, state):
        # rospy.loginfo(state)
        self.ps_pub.publish(state)
        return
        
    def l1Publish(self, state):
        # rospy.loginfo(state)
        self.l1_pub.publish(state)
        return
        
    def r1Publish(self, state):
        # rospy.loginfo(state)
        self.r1_pub.publish(state)
        return
