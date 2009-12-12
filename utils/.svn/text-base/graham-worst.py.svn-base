#!/usr/bin/env python

import random
import embaralha
import sys
from math import *

RADIUS = 10000

if len (sys.argv) < 2:
	print sys.argv[0],'<num-pts>'
	sys.exit (1)

num_pts = int (sys.argv[1])
if num_pts < 0: num_pts = - num_pts

l = [(0,0), (-2 * RADIUS, 0), (0, RADIUS)]

delta = (pi*5./40) /int (num_pts - 3)
theta = 35*pi/40
for i in range (0, int (num_pts - 3)):

	x = int (RADIUS * cos (theta))
	y = int (RADIUS * sin (theta))

	l.append ((x,y))
	theta = theta + delta

l = embaralha.embaralha (l)

for i in l:
	print i[0],i[1]
