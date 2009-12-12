#!/usr/bin/env python
"""Algoritmo de Graham"""

from geocomp.common.polygon import Polygon
from geocomp.common import control
from geocomp.common.guiprim import *


def Graham (l):
	"Algoritmo de Graham para achar o fecho convexo de uma lista l de pontos"

	if len (l) == 0: return None

	# So um ponto foi passado. Retorna um fecho c/ apenas um ponto
	if len (l) == 1:
		ret = Polygon (l)
		ret.plot ()
		ret.extra_info = 'vertices: 1'
		return ret

	p0 = l[0]

	# acha o ponto mais baixo
	for i in range (1, len(l)):
		if l[i].y < p0.y:
			p0 = l[i]
		elif l[i].y == p0.y:
			if l[i].x > p0.x:
				p0 = l[i]

	l.remove (p0)

	def cmp (x, y, z = p0):
		"""Funcao para ordenar os pontos ao redor de z

		Usada com a funcao sort, ordena os pontos de uma lista
		de acordo com o angulo que cada ponto forma com o ponto 
		z e a reta horizontal. Em caso de empate, o ponto mais
		distante aparece primeiro."""
		area = area2 (z, x, y)
		if area > 0:
			return -1
		elif area < 0:
			return 1
		else:
			dist_z_x = dist2 (z, x)
			dist_z_y = dist2 (z, y)
			if dist_z_y < dist_z_x:
				return -1
			return dist_z_y > dist_z_x

	# Ordena os pontos pelo seus angulos
	l.sort (cmp)

	# eliminando pontos colineares
	l2 = [ l[0] ]
	for i in range (1, len (l)):
		if collinear (p0, l[i-1], l[i]):
			continue
		l2.append (l[i])

	l = l2

	# So sobraram dois pontos -> retorna fecho c/ os dois
	if len (l) < 2:
		ret = Polygon ( [ p0, l[0] ] )
		ret.plot ()
		ret.extra_info = 'vertices: 2'
		return ret

	pilha = [ p0, l[0], l[1] ]

	p0.lineto (l[0])
	l[0].lineto (l[1])
	control.sleep ()

	for i in range (2, len(l)):
		l[i].hilight ()
		pilha[-1].lineto (l[i])
		control.sleep ()

		while not left (pilha[-2], pilha[-1], l[i]):
			pilha[-2].remove_lineto (pilha[-1])
			pilha[-1].remove_lineto (l[i])

			pilha.pop ()

			pilha[-1].lineto (l[i])
			control.sleep ()


		pilha.append (l[i])

		l[i].unhilight ()
		
	pilha[-1].lineto (pilha[0])
	

	for i in range (0, len(pilha)-1):
		pilha[i].remove_lineto (pilha[i+1])

	pilha[-1].remove_lineto (pilha[0])
	poligono = Polygon (pilha)
	poligono.plot ()
	control.thaw_update ()

	poligono.extra_info = 'vertices: %d'%len (poligono.to_list ())
	return poligono
