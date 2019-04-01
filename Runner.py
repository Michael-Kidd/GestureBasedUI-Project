from __future__ import print_function

import enum
import re
import struct
import sys
import threading
import time

import serial
from serial.tools.list_ports import comports

import robohat

from myo_raw import BT, MyoRaw
from PyoConnect import *


def onPoseEdge(p):

	if p == p.REST:
<<<<<<< HEAD
		#print("Rest")
		robohat.stop()
		myo.rotSetCenter()
		#robohat.cleanup()
	elif p == p.FIST:
		#print("Fist")
		#if myo.getBox() == 7:
		#	print("Turn Left")
		#	robohat.turnForward(0, speed)
		#elif myo.getBox() == 3:
		#	print("Turn Right")
		#	robohat.turnForward(speed, 0)
		#else:
		#print("forward")
		robohat.forward(speed)
	elif p == p.WAVE_OUT:
		#print("Spin Right")
		robohat.spinRight(speed)
		myo.rotSetCenter()
	elif p == p.WAVE_IN:
		#print("Spin Left")
		robohat.spinLeft(speed)
		myo.rotSetCenter()
	elif p == p.FINGERS_SPREAD:
		#print("Reverse")
		robohat.reverse(speed)
		myo.rotSetCenter()
=======
		print("Rest")
		robohat.stop()
		myo.rotSetCenter()
		#robohat.cleanup()
	if p == p.FIST:
		print("Fist")
		if myo.getBox() == 7:
			print("Turn Left")
			robohat.turnForward(0, speed)
		elif myo.getBox() == 3:
			print("Turn Right")
			robohat.turnForward(speed, 0)
		else:
			print("forward")
			robohat.forward(speed)
	if p == p.WAVE_OUT:
		print("Spin Right")
		robohat.spinRight(speed)
		myo.rotSetCenter()
	if p == p.WAVE_IN:
		print("Spin Left")
		robohat.spinLeft(speed)
		myo.rotSetCenter()
	if p == p.FINGERS_SPREAD:
		print("Reverse")
		robohat.reverse(speed)
		myo.rotSetCenter()
>>>>>>> 6e7ce5c966e6548a9ddd86e85382bf5348630b5e

if __name__ == '__main__':

	# Connect the myo armband
<<<<<<< HEAD
	myo = Myo(sys.argv[1] if len(sys.argv) >= 2 else None) 

	speed = 80
=======
	myo = Myo(sys.argv[1] if len(sys.argv) >= 2 else None)

	speed = 40
>>>>>>> 6e7ce5c966e6548a9ddd86e85382bf5348630b5e
	myo.connect()
	robohat.init()
	# arm handler, left and right arms
	# also handles the direction, either facing elbow or wrist
	# myo.add_arm_handler(lambda arm, xdir: print('arm', arm, 'xdir', xdir))
	myo.add_pose_handler(lambda p: onPoseEdge(p))
	while True:
		# keep the Myo active
		myo.run()
