#!/usr/bin/env python

# Simple motor teleop handler
import rospy
from std_msgs.msg import Int16

import sys, termios, tty, os, time

# Basic settings
button_delay = 0.2
speed = 200

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
    lmotor_pub = rospy.Publisher('lmotor', Int16, queue_size=10)
    rmotor_pub = rospy.Publisher('rmotor', Int16, queue_size=10)
    rospy.init_node('zumo_teleop_node', anonymous = False)
    rate = rospy.Rate(10)

    print("zumo_teleop_node starting now...")
    print("Press q to exit")

    while True:
        char = getch()

        if char == "q":
            print("Exiting teleop now...")
            exit(0)

        if char == "a":
            print("Left arrow was pressed")
            lmotor_pub.publish(-speed)
            rmotor_pub.publish(speed)
        elif char == "w":
            print("Up arrow was pressed")
            lmotor_pub.publish(speed)
            rmotor_pub.publish(speed)
        elif char == "d":
            print("Right arrow was pressed")
            lmotor_pub.publish(speed)
            rmotor_pub.publish(-speed)
        elif char == "s":
            print("Down arrow was pressed")
            lmotor_pub.publish(-speed)
            rmotor_pub.publish(speed)

        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
