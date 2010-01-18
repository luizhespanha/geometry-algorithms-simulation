#!/usr/bin/env python

from math import *
import sys

RADIUS = 100

def randspiral_radius (num_pts, num_turns):

	l = []
	b = 3.32614159909e-2
	radius_max = RADIUS*exp (b*2*pi*num_turns)
	log_a = log (100)
	theta = 0
	radius = RADIUS
	for i in range (num_pts):
		radius = float (i)/num_pts * radius_max + 100
		theta = (log (radius) - log_a) / b

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

	l = randspiral_radius (num_pts, num_turns)

	for p in l:
		print p[0],p[1]
