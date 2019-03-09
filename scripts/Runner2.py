from __future__ import print_function
from myo_raw import *
from Stepper_Motor_HAT_Code.python.DRV8825 import DRV8825
#from LightMatrix import *
import tty
import sys
import termios
import threading
import time
import RPi.GPIO as GPIO

def onPoseEdge(p):

	# Simple if statement to control based on gesture
	# As thos is not suited to the hardware we have it will not be used
	# therefore i wont mulithread the code - only using it as a reference and to show body of work
	if p == p.REST:
		stopLeft()
		stopRight()
		#print("rest")
	if p == p.FIST:
		leftMotor("forward")
		rightMotor("forward")
		#print("fist")
	if p == p.WAVE_OUT:
		rightMotor("forward")
		#print("Wave Out")
	if p == p.WAVE_IN:
		leftMotor("forward")
		#print("Wave In")
	if p == p.FINGERS_SPREAD:
		leftMotor("backward")
		rightMotor("backward")
		#print("Spread Fingers")


def leftMotor(direction):
	# Move the left motor in a direction
	Motor1.TurnStep(Dir=direction, steps=2048, stepdelay=0.0002)

def rightMotor(direction):	
	# Move the right motor in a direction
	Motor2.TurnStep(Dir=direction, steps=2048, stepdelay=0.0002)

def stopLeft():
	# stop the left Motor
	Motor1.Stop()

def stopRight():	
	# Stop the right motor
	Motor2.Stop()	

if __name__ == '__main__':
	
	# Initialise the left and right motors
	# the dir pin, will trigger the motor to turn in the opposite direction
	# the step pin is used by the step motor to create intervals - turns out this type of motor is not used for wheels
	# the enable pin , wakes the motor up
	# the mode pins are used for other stepping functions

	Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
	Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

	# determines the stepping method, can be hardware or software based on the motor
	# can be fullstep or halfstep
	Motor1.SetMicroStep('hardward' ,'fullstep')
	Motor2.SetMicroStep('hardward' ,'fullstep')

	# Connect the myo armband
	m = MyoRaw(sys.argv[1] if len(sys.argv) >= 2 else None)
	m.connect()

	# arm handler, left and right arms
	# also handles the direction, either facing elbow or wrist
	m.add_arm_handler(lambda arm, xdir: print('arm', arm, 'xdir', xdir))
	m.add_pose_handler(lambda p: onPoseEdge(p))

	while True:
		# keep the Myo active
		m.run()