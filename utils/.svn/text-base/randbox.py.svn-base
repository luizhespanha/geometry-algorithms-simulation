#!/usr/bin/env python

import random

def randbox (num_pts, side_length):
	l = []
	for i in range (0, num_pts):
		x = float (random.uniform (0, side_length))
		y = float (random.uniform (0, side_length))

		l.append ( (x, y) )
	
	return l

if __name__ == '__main__':
	import sys
	LENGTH = 100

	if len (sys.argv) < 2:
		print sys.argv[0],'<num> [length]'
		sys.exit (1)

	if len (sys.argv) > 2:
		if int (sys.argv[2]) > 0:
			LENGTH = int (sys.argv[2])

	l = randbox (int (sys.argv[1]), LENGTH)

	for p in l:
		print p[0],p[1]
