# Imports to import fucntions for the Myo Armband
from __future__ import print_function

import sys
import threading
#from LightMatrix import *
from myo_raw import *
from Stepper_Motor_HAT_Code.python.DRV8825 import DRV8825
import RPi.GPIO as GPIO

def onPoseEdge(p):
	if p == p.REST:
		#clear()
		#print("rest")
		stopLeft()
		stopRight()
	else:	
		if p == p.FIST:
			#forward(0, 0, 255)
			#print("fist")
			threading.Thread(target=leftMotor('forward')).start()
			threading.Thread(target=rightMotor('forward')).start()
		elif p == p.WAVE_OUT:
			rightMotor('forward')
			#reverse(255, 0, 0)
			#print("Wave Out")
		elif p == p.WAVE_IN:
			leftMotor('forward')
			#reverse(255, 0, 0)
			#print("Wave In")


def leftMotor(direction):
	Motor1.TurnStep(Dir=direction, steps=1024, stepdelay=0.0001)

def rightMotor(direction):	
	Motor2.TurnStep(Dir=direction, steps=1024, stepdelay=0.0001)

def stopLeft():
	Motor1.Stop()

def stopRight():	
	Motor2.Stop()	

if __name__ == '__main__':
	# clear()
	# Took this from the Myo_raw file which connects the myo
	# this will allow the script to connect to the armband

	Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
	Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))
	Motor1.SetMicroStep('hardward' ,'fullstep') 
	Motor2.SetMicroStep('hardward' ,'fullstep') 

	m = MyoRaw(sys.argv[1] if len(sys.argv) >= 2 else None)
	m.connect()

	m.add_arm_handler(lambda arm, xdir: print('arm', arm, 'xdir', xdir))
	m.add_pose_handler(lambda p: onPoseEdge(p))

	while True:
		m.run()