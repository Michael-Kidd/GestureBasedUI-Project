# Imports to import fucntions for the Myo Armband
from __future__ import print_function

import enum
import re
import struct
import sys
import threading
import time
import serial
from serial.tools.list_ports import comports
from LightMatrix import *
from myo_raw import BT, MyoRaw

def onPoseEdge(p):

	print(p)

	if p == p.REST:
		'''myo.rotSetCenter()'''
		clear()
	if p == p.FIST:
		forward(0, 0, 255)
	if p == p.WAVE_OUT:
		reverse(255, 0, 0)



if __name__ == '__main__':
	clear()
	# Took this from the Myo_raw file which connects the myo
	# this will allow the script to connect to the armband
	m = MyoRaw(sys.argv[1] if len(sys.argv) >= 2 else None)
	m.connect()

	m.add_arm_handler(lambda arm, xdir: print('arm', arm, 'xdir', xdir))
	m.add_pose_handler(lambda p: onPoseEdge(p))

	while True:
		m.run()