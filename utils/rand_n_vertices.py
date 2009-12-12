#!/usr/bin/env python

import randdisc
import uniform_circ
import random
import embaralha

def rand_n_vertices (num_pts, num_vertices, radius):
	if radius < 0: radius = -radius
	if radius == 0: radius = 10000

	if num_vertices < 4: num_vertices = 4

	if num_vertices > num_pts:
		num_vertices, num_pts = num_pts, num_vertices
	
	l1 = randdisc.randdisc (num_pts - num_vertices, 0.7*radius)
	l2 = uniform_circ.uniform_circ (num_vertices, radius)

	l1.extend (l2)

	return embaralha.embaralha (l1)

if __name__ == '__main__':
	import sys
	RADIUS = 10000

	if len (sys.argv) < 3:
		print sys.argv[0],'<num_pts> <num_vertices> [radius]'
		print '"radius" é multiplicado internamente por 0.7'
		sys.exit (1)

	num_pts = int (sys.argv[1])
	num_vertices = int (sys.argv[2])

	if len (sys.argv) > 3:
		RADIUS = float (sys.argv[3])

	l = rand_n_vertices (num_pts, num_vertices, RADIUS)

	for p in l:
		print p[0],p[1]
