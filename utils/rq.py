#!/usr/bin/env python

import random
from math import *

def rq (num_pts, radius):
	if radius < 0: radius = -radius
	if radius == 0: radius = 15000
	l = []
	theta = pi/2
	for i in range (0, num_pts):
		x = float (radius * cos (theta))
		y = float (radius * sin (theta))

		l.append ((x, y))
		theta = theta/2
	
	x = float (radius * cos (0))
	y = float (radius * sin (0))
	l.append ((x, y))
	return l

if __name__ == '__main__':
	import sys
	RADIUS = 15000

	if len (sys.argv) < 2:
		print sys.argv[0],'<num> [radius]'
		sys.exit (1)

	if len (sys.argv) > 2:
		if int (sys.argv[2]) > 0:
			RADIUS = int (sys.argv[2])

	l = rq (int (sys.argv[1]), RADIUS)

	for p in l:
		print p[0],p[1]
