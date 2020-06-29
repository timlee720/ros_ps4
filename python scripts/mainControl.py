#! /usr/bin/python

'''
Usage: 
# Subscribe ROS Joystick Topic ('/joy') to read PS4 Controller values
# Subscribe OpenCV linear velocity values 
# Map each input (button & joystick) to corresponding function
'''

import rospy
import signal
import sys
from decimal import *
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from rosPub import Talker
import velocityCalc as vel

def signalHandler(signal, frame): 
    # Ctrl + C --> Exit program
    print('\nYou pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signalHandler)


class ps4Controller:
    def __init__(self):
        rospy.init_node('ps4Talker', anonymous = True)
        rospy.Subscriber('/joy', Joy, self.callback)
        rospy.Subscriber('/opencv', Twist, self.opencvCallback)
        self.rate = rospy.Rate(20)
        self.pub = Talker()

        # Essential variables for button states
        self.cross_state = False
        self.circle_state = False
        self.tri_state = False
        self.square_state = False

        self.l1_state = False
        self.r1_state = False

        self.share_state = False
        self.option_state = False
        self.ps_state = False

        # Velocity
        self.rightX = 0.0
        self.leftX = 0.0
        self.leftY = 0.0
    
    def callback(self, data):
        if(data.buttons[0] != self.cross_state):
            self.cross_state = data.buttons[0]
            self.crossCallback(self.cross_state)

        elif(data.buttons[1] != self.circle_state):
            self.circle_state = data.buttons[1]
            self.circleCallback(self.circle_state)

        elif(data.buttons[2] != self.tri_state):
            self.tri_state = data.buttons[2]
            self.triCallback(self.tri_state)

        elif(data.buttons[3] != self.square_state):
            self.square_state = data.buttons[3]
            self.squareCallback(self.square_state)
        
        elif(data.buttons[4] != self.l1_state):
            self.l1_state = data.buttons[4]
            self.l1Callback(self.l1_state)
        
        elif(data.buttons[5] != self.r1_state):
            self.r1_state = data.buttons[5]
            self.r1Callback(self.r1_state)

        elif(data.buttons[8] != self.share_state):
            self.share_state = data.buttons[8]
            self.shareCallback(self.share_state)

        elif(data.buttons[9] != self.option_state):
            self.option_state = data.buttons[9]
            self.optionCallback(self.option_state)

        elif(data.buttons[10] != self.ps_state):
            self.ps_state = data.buttons[10]
            self.psCallback(self.ps_state)

        else:
            # if(not self.l1_state):
            #     vel.manualMode(data.axes[0], data.axes[1], data.axes[3], data.axes[7])
            # else:
            #     self.rightX = data.axes[3]
            #     vel.autoMode(self.leftX, self.leftY, self.rightX)
            pass

        '''
        # Axes value
        # Left joystick
        # data.axes[0]: left-right  data.axes[1]: up-down
        # Right joystick
        # data.axes[3]: left-right  data.axes[4]: up-down
        # Arrows value
        # data.axes[7]: up-down     data.axes[6]: left-right 
        '''
        if(not self.l1_state):
            vel.manualMode(data.axes[0], data.axes[1], data.axes[3], data.axes[7])
        else:
            self.rightX = data.axes[3]
            vel.autoMode(self.leftX, self.leftX, self.rightX)
            
        return

    def opencvCallback(self, twistData):
        print(twistData)
        if(self.l1_state):
            self.leftX = twistData.linear.y
            self.leftY = twistData.linear.x
            # vel.autoMode(twistData.linear.y, twistData.linear.x, self.rightX)
        
        return


    def crossCallback(self, state):
        if(state == True):
            print("\n***** Kick Stage 1 *****")

        print("Cross is {}".format(state))
        self.pub.crossPublish(state)
        return


    def circleCallback(self, state):
        if(state == True):
            print("\n***** Kick Stage 2 *****")

        print("Circle is: {}".format(state))
        self.pub.circlePublish(state)
        return


    def triCallback(self, state):
        if(state == True):
            print("\n***** Push *****")
        
        print("Triangle is: {}".format(state))
        self.pub.triPublish(state)
        return

    
    def l1Callback(self, state):
        print("L1 is: {}".format(state))
        if(not state):
            print('***** End Automation *****')
        else:
            print("***** Automation *****")
        self.pub.l1Publish(state)
        return

    
    def r1Callback(self, state):
        print("R1 is: {}".format(state))
        self.pub.r1Publish(state)
        return

    
    def squareCallback(self, state):
        print("Square is: {}".format(state))
        self.pub.squarePublish(state)
        return

    
    def optionCallback(self, state):
        if(state):
            print("Reset")
        print("Options is: {}".format(state))
        self.pub.optionPublish(state)
        return

    
    def shareCallback(self, state):
        print("Share is: {}".format(state))
        self.pub.sharePublish(state)
        return

    
    def psCallback(self, state):
        print("PlayStation is: {}".format(state))
        self.pub.psPublish(state)
        return



if __name__ == '__main__':
    print("start reading ps4 controller events")
    myPS4 = ps4Controller()
    rospy.spin()
