#!/usr/bin/env python

import random
from math import *

def randdisc (num_pts, radius):
	if radius < 0: radius = -radius
	if radius == 0: radius = 10000
	l = []
	for i in range (0, num_pts):
		r2 = random.uniform (0, radius*radius)
		r = sqrt (r2)
		theta = random.uniform (0, 2 * pi)

		x = float (r * cos (theta))
		y = float (r * sin (theta))

		l.append ( (x,y) )
	
	return l


if __name__ == '__main__':
	import sys
	RADIUS = 10000

	if len (sys.argv) < 2:
		print sys.argv[0],'<num> [radius]'
		sys.exit (1)

	if len (sys.argv) > 2:
		if int (sys.argv[2]) > 0:
			RADIUS = float (sys.argv[2])

	l = randdisc (int (sys.argv[1]), RADIUS)

	for p in l:
		print p[0],p[1]
