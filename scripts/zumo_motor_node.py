#!/usr/bin/env python

# Simple motor instruction handler
import rospy
import zumo
from zumoros.msg import motor

def motorHandler(data):
    zumo.setMotors(rmotor = data.rmotor, 
                   lmotor = data.lmotor, 
                   rdir = data.rdir, 
                   ldir = data.ldir)

def main():
    rospy.init_node('zumo_motor_node', anonymous = False)
    rospy.Subscriber('zumo_motors', motor, motorHandler)
    zumo.init(9600, '/dev/ttyUSB0')

    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        # Used for shutdown safely
        zumo.deinit()
        pass
