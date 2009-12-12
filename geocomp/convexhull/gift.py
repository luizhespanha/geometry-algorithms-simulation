#!/usr/bin/env python
"""Algoritmo Embrulho para Presente"""

from geocomp.common.polygon import Polygon
from geocomp.common import control
from geocomp.common.guiprim import *

def Gift (l):
	"Algoritmo Embrulho para Presente para encontrar o fecho convexo de uma lista l de pontos"

	# achando ponto mais baixo
	i0 = 0
	for i in range (1, len(l)):
		if l[i].y < l[i0].y:
			i0 = i
		elif l[i].y == l[i0].y:
			if l[i].x > l[i0].x:
				i0 = i
	
	fecho = [ l[i0] ]
	n = len (l)
	i = i0
	while 1:
		# passo embrulho para presente
		j0 = 0
		for j in range (1,n):
			if j == i:
				continue
			direction = area2 (l[i], l[j0], l[j])
			if direction < 0:
				j0 = j
			elif direction == 0:
				if dist2 (l[i], l[j0]) < dist2 (l[i], l[j]):
					j0 = j

		i = j0
		fecho[-1].lineto (l[j0])
		if (i == i0):
			break
		fecho.append (l[j0])
	
	ch = Polygon (fecho)
	ch.extra_info = 'vertices: %d'%len (fecho)
	return ch
