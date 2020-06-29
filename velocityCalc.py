#! /usr/bin/python

'''
Usage:
# Calculate the velocity for both manual and automation mode
leftX : 
# Process OpenCV values and generate Twist value integrating 
    the manual input of angular z value
'''

from geometry_msgs.msg import Twist
from rosPub import Talker
scale_linear = -15.0
scale_angular = -22.0
isForward = 1
vel_msg = Twist()


def manualMode(leftX, leftY, rightX, arrowY):
    global scale_linear
    global scale_angular
    global isForward
    global vel_msg

    deadBand = 0.05

    print("\n***** Manual Mode *****")

    vel_msg.angular.z = rightX * scale_angular

    if(arrowY != 0.0):
        vel_msg.linear.x = 1.5 * scale_linear * isForward
    elif(leftY <= deadBand and leftY >= -deadBand):
        vel_msg.linear.x = 0.0
    elif (leftY < -deadBand):
        vel_msg.linear.x = (-leftY + deadBand) / (1 - deadBand) * 1.5 * scale_linear * isForward
    elif (leftY > deadBand):
        vel_msg.linear.x = (-leftY - deadBand) / (1 - deadBand) * 1.5 * scale_linear * isForward

    if(leftX <= deadBand and leftX >= -deadBand):
        vel_msg.linear.y = 0.0
    elif(leftX < -deadBand):
        vel_msg.linear.y = (leftX + deadBand) / (1 - deadBand) * 0.8 * scale_linear * isForward
    elif(leftX > deadBand):
        vel_msg.linear.y = (leftX - deadBand) / (1 - deadBand) * 0.8 * scale_linear * isForward
        
    pub = Talker()
    pub.manualPublish(vel_msg)
    return

def autoMode(leftX, leftY, rightX):
    global scale_angular

    vel_msg.angular.z = rightX * scale_angular * 0.3
    vel_msg.linear.y = leftX
    vel_msg.linear.x = leftY

    pub = Talker()
    pub.autoPublish(vel_msg)
    return

