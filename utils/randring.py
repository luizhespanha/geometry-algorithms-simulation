#!/usr/bin/env python

import random
from math import *

def randring (num_pts, radius1, radius2):
	if radius1 < 0: radius1 = - radius1
	if radius2 < 0: radius2 = - radius2
	if radius1 > radius2:
		(radius1, radius2) = (radius2, radius1)

	l = []
	for i in range (0, num_pts):
		r2 = random.uniform (radius1*radius1, radius2*radius2)
		r = sqrt (r2)
		theta = random.uniform (0, 2 * pi)

		x = float (r * cos (theta))
		y = float (r * sin (theta))

		l.append ( (x, y) )
	
	return l

if __name__ == '__main__':
	import sys

	RADIUS1 =  9000
	RADIUS2 = 10000

	if len (sys.argv) < 2:
		print sys.argv[0],'<num-pts> [radius1] [radius2]'
		sys.exit (1)

	num_pts = int (sys.argv[1])
	if len (sys.argv) > 2:
		RADIUS1 = float (sys.argv[2])
		if len (sys.argv) > 3:
			RADIUS2 = float (sys.argv[3])
	
	l = randring (num_pts, RADIUS1, RADIUS2)

	for p in l:
		print p[0], p[1]
