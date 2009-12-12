#!/usr/bin/env python
"Algoritmo Incremental Probabilistico"

import random
from geocomp.common.point import Point
from geocomp.common.polygon import Polygon
from geocomp.common import control
from geocomp.common.guiprim import *
from geocomp import config

# l[k], O, p, p.next
def intersect_restricted (a, b, c, d):
	"""Verdadeiro se ab intersecta cd

	NAO FUNCIONA NO CASO GERAL:
	Ela admite que left (c, d, b) == TRUE. Alem disso,
	ela so' retorna verdadeiro se collinear (c, d, a) == FALSE"""
	a_x = min (a.x, b.x)
	a_y = min (a.y, b.y)
	b_x = max (a.x, b.x)
	b_y = max (a.y, b.y)

	c_x = min (c.x, d.x)
	c_y = min (c.y, d.y)
	d_x = max (c.x, d.x)
	d_y = max (c.y, d.y)

	if not (a_x <= d_x and c_x <= b_x and a_y <= d_y and c_y <= b_y):
		return 0

	# left (c, d, b) == TRUE!
	abc = area2 (a, b, c)
	abd = area2 (a, b, d)
	cda = area2 (c, d, a)

	return (abd != 0) and (abc > 0) != (abd > 0) and not (cda >= 0)
	
	

def vertices_tangentes (intersect, p):
	"""retorna os vertices de tangencia do poligono a que intersect pertence em relacao a p

	Admite que o segmento de intersect a intersect.next e' visivel por p"""

	tan = []
	arestas = []

	pts = intersect
	while right_on (pts.prev, pts, p):
		pts = pts.prev
	tan.append (pts)

	pts = intersect
	while right_on (pts, pts.next, p):
		pts = pts.next
	tan.append (pts)

	return tan

	
def classify (convex, points, start):
	"Associa cada ponto em points a uma aresta visivel do triangulo convex"

	first = convex.pts
	second = first.next
	third = second.next
	first.L = []
	second.L = []
	third.L = []

	# O e' um ponto dentro do fecho convexo (que ainda e' um triangulo)
	Ox = (first.x + second.x + third.x) / 3.0
	Oy = (first.y + second.y + third.y) / 3.0
	O = Point (Ox, Oy)
	O.hilight (config.COLOR_ALT2)

	for i in range (start, len (points)):
		for p in (first, second, third):
			points[i].interior = 1
			if intersect_restricted (points[i], O, p, p.next):
				p.L.append (points[i])
				points[i].intersect = p
				points[i].interior = 0
				points[i].lineto (p, config.COLOR_ALT1)
				break
	
	return O
				

def IncrProb (l):
	"Algoritmo incremental probabilistico para encontrar o fecho convexo"

	if len (l) == 0: return None

	# Embaralhando o vetor de entrada
	for i in range (len (l) -1, -1, -1):
		index = int (random.uniform (0, i+1))
		aux = l[i]
		l[i] = l[index]
		l[index] = aux
	
	# Inicializando alguns campos...
	for i in range (0, len(l)):
		l[i].L = []
		l[i].interior = 0
		

	# Criando um fecho convexo com 1 ponto
	fecho = Polygon ([ l[0] ])
	fecho.plot ()
	
	length = 1
	k = 0
	hi = l[k].hilight ()
	# Como nao posso admitir que os pontos estao em posicao geral,
	#  preciso tomar cuidado ate' conseguir um fecho convexo com
	#  3 pontos
	for k in range (1, len (l)):
		pts = fecho.pts
		l[k-1].unhilight (hi)
		hi = l[k].hilight ()
		control.thaw_update ()
		if length == 1:
			if l[k].x == pts.x and l[k].y == pts.y:
				continue
			fecho.hide ()
			pts.next = pts.prev = l[k]
			l[k].next = l[k].prev = pts
			fecho.pts = pts
			fecho.plot ()
			length = length + 1
		
		elif length == 2:
			next = pts.next
			dir = area2 (pts, next, l[k])
			if dir == 0:
				#Mais um ponto colinear -> pega o par mais distante
				fecho.hide ()
				dist_pts_next = dist2 (pts, next)
				dist_pts_lk = dist2 (pts, l[k])
				dist_next_lk = dist2 (next, l[k])
				if dist_pts_next >= dist_pts_lk and dist_pts_next >= dist_next_lk:
					a = pts
					b = next
				elif dist_pts_lk >= dist_pts_next  and  dist_pts_lk >= dist_next_lk:
					a = pts
					b = l[k]
				elif dist_next_lk >= dist_pts_lk and dist_next_lk >= dist_pts_next:
					a = next
					b = l[k]
				else:
					print 'pau!!!'

				a.next = a.prev = b
				b.next = b.prev = a
				fecho.pts = a
				fecho.plot ()

				continue
			fecho.hide ()
			# Um ponto /nao/ colinear :) -> tomar cuidado com a 
			#  orientacao
			if dir > 0:
				pts.prev = next.next = l[k]
				l[k].next = pts
				l[k].prev = next
			else:
				pts.next = next.prev = l[k]
				l[k].prev = pts
				l[k].next = next

			length = length + 1
			fecho.pts = pts
			fecho.plot ()
			O = classify (fecho, l, k)
			break

	# Ja temos um fecho com 3 pontos -> basta cresce-lo
	for k in range (k+1, len (l)):
		pts = fecho.pts
		l[k-1].unhilight (hi)
		hi = l[k].hilight ()
		control.thaw_update ()

		if l[k].interior:
			control.sleep ()
			continue

		l[k].remove_lineto (l[k].intersect)
		control.sleep ()

		tan = vertices_tangentes (l[k].intersect, l[k])

		l[k].intersect.L.remove (l[k])

		l0 = []
		l1 = []
		# atualizando a classificacao dos pontos
		vertex = tan[0]
		while vertex != tan[1]:
			for p in vertex.L:
				id = p.hilight (config.COLOR_ALT3)
				p.remove_lineto (p.intersect)

				if p == l[k]:
					p.unhilight (id)
					continue

				if left (l[k], O, p):
					if left_on (tan[0], l[k], p):
						p.interior = 1
						p.intersect = None
					else:
						p.intersect = tan[0]
						p.lineto (p.intersect, config.COLOR_ALT1)
						l0.append (p)
				else:
					if left_on (l[k], tan[1], p):
						p.interior = 1
						p.intersect = None
					else:
						p.intersect = l[k]
						p.lineto (p.intersect, config.COLOR_ALT1)
						l1.append (p)

				p.unhilight (id)

			vertex = vertex.next

		tan[0].L = l0
		l[k].L = l1

		# atualizando o fecho
		control.freeze_update ()
		fecho.hide ()

		tan[0].next.prev = None
		tan[0].next = l[k]
		l[k].prev = tan[0]

		if tan[1].prev: tan[1].prev.next = None
		tan[1].prev = l[k]
		l[k].next = tan[1]

		fecho.pts = tan[0]
		fecho.plot ()

		control.thaw_update ()

	l[k].unhilight (hi)
	fecho.plot ()
	fecho.extra_info = 'vertices: %d'%len (fecho.to_list ())
	return fecho

