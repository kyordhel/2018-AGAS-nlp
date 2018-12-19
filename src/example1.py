#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import math
import signal


import re
from robot import Robot

def parse(s):
	keywords = ['advance', 'step', 'turn', 'stop', 'spin']
	parts = re.split(r'\s+', s.lower())
	for word in parts:
		if word in keywords:
			return 'robot.{}()'.format(word)
	return None
#end def

def main():
	robot = Robot()
	while(True):
		s = raw_input('? ')
		if s in ['exit', 'quit', 'end']:
			robot.stop()
			sys.exit(1)
		action = parse(s)
		if not action is None:
			eval(action)
#end def





















def exit_gracefully(signum, frame):
	# restore the original signal handler as otherwise evil things will happen
	# in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
	signal.signal(signal.SIGINT, original_sigint)
	try:
		sys.exit(1)
	except KeyboardInterrupt:
		sys.exit(1)
	# restore the exit gracefully handler here    
	signal.signal(signal.SIGINT, exit_gracefully)


if __name__ == '__main__':
	original_sigint = signal.getsignal(signal.SIGINT)
	signal.signal(signal.SIGINT, exit_gracefully)
	main()
