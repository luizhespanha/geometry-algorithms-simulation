#!/usr/bin/env python

from math import *

RADIUS = 100

def randspiral (num_pts, num_turns):

	l = []
	theta = 0
	radius = RADIUS
	for i in range (num_pts):
		theta = i*(num_turns*2*pi)/num_pts
		radius = RADIUS * exp (3.32614159909e-2*theta)

		x = radius * cos (theta)
		y = radius * sin (theta)

		l.append ( (x, y) )
	
	return l

if __name__ == '__main__':
	import sys

	if len (sys.argv) != 3:
		print sys.argv[0],'<num_pts> <num_turns>'
		sys.exit (1)

	num_pts = int (sys.argv[1])
	num_turns = float (sys.argv[2])

	l = randspiral (num_pts, num_turns)

	for p in l:
		print p[0],p[1]
