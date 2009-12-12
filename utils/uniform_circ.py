#!/usr/bin/env python

import sys
from math import *

def uniform_circ (num_pts, radius):

	l = []

	for i in range (num_pts):
		theta = (2*pi*i)/num_pts

		x = float (radius * cos (theta))
		y = float (radius * sin (theta))

		l.append ( (x, y) )

	return l

if __name__ == '__main__':
	RADIUS = 10000

	if len (sys.argv) < 2:
		print sys.argv[0],'<num> [radius]'
		sys.exit (1)

	num_pts = int (sys.argv[1])
	if len (sys.argv) > 2:
		RADIUS = floar (sys.argv[2])
	
	l = uniform_circ (num_pts, RADIUS)

	for p in l:
		print p[0], p[1]

