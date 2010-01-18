#!/usr/bin/env python

import randdisc
import random
import embaralha

def randspecial1 (num_pts, radius):

	if radius < 0: radius = -radius
	l = randdisc.randdisc (num_pts - 2, 0.4*radius)
	l.append ( (-2*radius, -.55*radius) )
	l.append ( (2*radius, .45*radius) )

	return embaralha.embaralha (l)

if __name__ == '__main__':
	import sys
	RADIUS = 10000

	if len (sys.argv) < 2:
		print sys.argv[0],'<num> [radius]'
		print '"radius" é multiplicado internamente por 0.4'
		sys.exit (1)

	if len (sys.argv) > 2:
		RADIUS = int (sys.argv[2])

	l = randspecial1 (int (sys.argv[1]), RADIUS)

	for p in l:
		print p[0],p[1]
