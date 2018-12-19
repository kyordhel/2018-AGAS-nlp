#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import math
import signal


import nltk
from robot import Robot
robot = Robot()

def parse(s):
	parts = nltk.word_tokenize(s.lower())
	stemmer = nltk.stem.SnowballStemmer('english')
	for word in parts:
		switcher = {
			'turn'    : "turn({})".format(parts),
			'walk'    : "robot.advance(0.5)",
			'run'     : "robot.advance(1.5)",
			'advance' : "robot.advance()",
			'stop'    : "robot.stop()",
			'spin'    : "robot.spin()",
		}
		func = switcher.get(stemmer.stem(word), None)
		if not func is None:
			return func
	return None
#end def

def turn(parts):
	if 'left' in parts:
		robot.rotate(90)
	elif 'right' in parts:
		robot.rotate(-90)
	else:
		robot.turn()
#end def
	

def main():
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
