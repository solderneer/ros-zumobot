#!/usr/bin/env python

# This module provides methods to access the zumobot interface
# Copied from my unit test code at https://github.com/solderneer/zumobot-serial-protocol

import serial
import time

ser = serial.Serial() # Global serial handle

def init(baudrate, port):
    global ser
    ser.baudrate = baudrate
    ser.port = port

    ser.open()

    if ser.is_open:
        return True
    else:
        return False

# Takes a value between 0 and 200 and maps it to each of the motors
def setMotors(rmotor, lmotor, rdir, ldir):
    startByte = 128
    global ser

    if(rdir == True) and (ldir == True):
        startByte = startByte + 3
    elif rdir == True:
        startByte = startByte + 1
    elif ldir == True:
        startByte = startByte + 2
    else:
        pass

    if (-200<lmotor<200) and (-200<rmotor<200):
        ser.write(startByte)
        ser.write(lmotor)
        ser.write(rmotor)
        return True
    else:
        return False

def selftest():
    init(9600, '/dev/ttyMFD1')

    while True:
        zumo.setMotors(50,50,True,False)
        time.sleep(1)
        zumo.setMotors(50,50,False, True)

if __name__ = "__main__":
    selftest()

