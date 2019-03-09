# Imports to import fucntions for the Myo Armband
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
	if p == p.REST:
		print("rest")
	if p == p.FIST:
		print("fist")
	if p == p.WAVE_OUT:
		print("Wave Out")
	if p == p.WAVE_IN:
		print("Wave In")


def leftMotor(direction):
	Motor1.TurnStep(Dir=direction, steps=2048, stepdelay=0.0002)

def rightMotor(direction):	
	Motor2.TurnStep(Dir=direction, steps=2048, stepdelay=0.0002)

def stopLeft():
	Motor1.Stop()

def stopRight():	
	Motor2.Stop()	

def ConnectMyo():
	m = MyoRaw(sys.argv[1] if len(sys.argv) >= 2 else None)
	m.connect()

	m.add_arm_handler(lambda arm, xdir: print('arm', arm, 'xdir', xdir))
	m.add_pose_handler(lambda p: onPoseEdge(p))

	while True:
		m.run()

if __name__ == '__main__':
	
	Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
	Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

	Motor1.SetMicroStep('hardward' ,'fullstep')
	Motor2.SetMicroStep('hardward' ,'fullstep')

	Motor1.TurnStep(Dir='forward', steps=2048, stepdelay=0.0002)
	time.sleep( 5 )
	Motor1.Stop()