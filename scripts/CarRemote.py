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

from common import *

def onPoseEdge(pose, edge):
	print("onPoseEdge: "+pose+", "+edge)
