from __future__ import print_function
from myo_raw import * # Myo Import
from LightMatrix import * # our class for the Sense Hat Matrix
import tty
import sys
import termios
import threading # needed for multi threading
import RPi.GPIO as GPIO # used for accessing the GPIO pins on raspberry pi

def onPoseEdge(p):

	if p == p.REST:
		print("Stop")
		clearLights()
	if p == p.FIST:
		print("Drive")
		forwardLight(0, 0, 255)
	if p == p.WAVE_OUT:
		reverseLight(255, 0, 0)
		print("Reverse")

if __name__ == '__main__':

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