from __future__ import print_function
import enum
import re
import struct
import sys
import threading
import time
import serial
from serial.tools.list_ports import comports
from myo_raw import BT, MyoRaw

from PyoConnect import *

def onPoseEdge(p):

	if p == p.REST:
		myo.rotSetCenter()
		print("MYo Connected")
	if p == p.FIST:
		if myo.getBox() == 7:
			myo.vibrate(3)
			print("MYo Left?")
		elif myo.getBox() == 3:
			myo.vibrate(4)
			print("MYo Right?")
		else:
			myo.vibrate(2)
	if p == p.WAVE_OUT:
		myo.vibrate(1)


if __name__ == '__main__':

	# Connect the myo armband
	myo = Myo(sys.argv[1] if len(sys.argv) >= 2 else None) 
	print("MYo Connect")
	myo.connect()

	# arm handler, left and right arms
	# also handles the direction, either facing elbow or wrist
	# myo.add_arm_handler(lambda arm, xdir: print('arm', arm, 'xdir', xdir))
	myo.add_pose_handler(lambda p: onPoseEdge(p))

	while True:
		# keep the Myo active
		myo.run()