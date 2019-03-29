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
		robohat.stop()
		myo.rotSetCenter()
	if p == p.FIST:
		if myo.getBox() == 7:
			turnForward(0, speed):
		elif myo.getBox() == 3:
			turnForward(speed, 0):
		else:
			robohat.forward(speed)
	if p == p.WAVE_OUT:
		robohat.spinRight(speed)
	if p == p.WAVE_IN:
		robohat.spinLeft(speed)
	if p == p.FINGERS_SPREAD:
		robohat.reverse(speed)


if __name__ == '__main__':

	# Connect the myo armband
	myo = Myo(sys.argv[1] if len(sys.argv) >= 2 else None) 

	speed = 40
	myo.connect()
	robohat.init()
	# arm handler, left and right arms
	# also handles the direction, either facing elbow or wrist
	# myo.add_arm_handler(lambda arm, xdir: print('arm', arm, 'xdir', xdir))
	myo.add_pose_handler(lambda p: onPoseEdge(p))
	while True:
		# keep the Myo active
		myo.run()
