from __future__ import print_function
from myo_raw import * # Myo Import
import sys
import threading # needed for multi threading

from PyoConnect import *

def onPoseEdge(p):

	if p == p.REST:
		myo.rotSetCenter()
		print("Stop")
	if p == p.FIST:
		print("Drive")
	if p == p.WAVE_OUT:
		print("Reverse")
	if myo.getBox() == 7:
		print("Left")
	if myo.getBox() == 3:
		print("Right")


if __name__ == '__main__':

	# Connect the myo armband
	myo = Myo(sys.argv[1] if len(sys.argv) >= 2 else None) 
	myo.connect()

	# arm handler, left and right arms
	# also handles the direction, either facing elbow or wrist
	myo.add_arm_handler(lambda arm, xdir: print('arm', arm, 'xdir', xdir))
	myo.add_pose_handler(lambda p: onPoseEdge(p))

	while True:
		# keep the Myo active
		myo.run()