from __future__ import print_function

from LightMatrix import * # our class for the Sense Hat Matrix
import sys
import threading # needed for multi threading
from PyoConnect import *

def onPoseEdge(p):

	if p == p.REST:
		myo.rotSetCenter()
		clearLights()
	if p == p.FIST:
		forwardLight(0, 0, 255)
	if p == p.WAVE_OUT:
		reverseLight(255, 0, 0)
	if myo.getBox() == 7:
		leftLight(0, 255, 0)
	if myo.getBox() == 3:
		rightLight(0, 255, 0)


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