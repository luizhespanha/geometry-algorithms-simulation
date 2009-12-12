#!/usr/bin/env python
"Algoritmo Incremental"

from geocomp.common.polygon import Polygon
from geocomp.common import control
from geocomp.common.guiprim import *


def vertices_tangentes (Q, p):
	"""retorna os dois vertices de tangencia de Q em relacao a p

	Se existirem (i.e. se p estiver fora de Q), os vertices de tangencia
	sao retornados em uma lista. Na posicao [0] dessa lista esta o vertice
	"anterior" a p, e na posicao 1 o vertice "posterior" a p.

	Se p estiver dentro de Q, retorna uma lista vazia."""

	tan = []
	arestas = []

	pts = Q.pts
	area_old = area2 (pts.prev, pts, p)
	last = (area_old >= 0) # left_on
	for pts in Q.to_list ():
		prev = pts.prev
		next = pts.next
		cur = pts

		area = area2 (cur, next, p)

		now = (area >= 0) # left_on
		if last != now:
			if area_old == 0: 
				# novo ponto e' colinear c/ aresta anterior
				#  --> pegamos verice mais distante
				tan.append (prev)
			elif area == 0:
				# novo ponto e' colinear c/ proxima aresta
				#  --> pegamos vertice mais distante
				tan.append (next)
			else:
				tan.append (cur)
		last = now
		area_old = area

	if len (tan) == 0:
		return []
	
	if len (tan) != 2:
		print '\n\n===> len (tan) != 0 e != 2 !!!!\n\n'

	if right (tan[0], tan[1], p):
		return [ tan[0], tan[1] ]
	else:
		return [ tan[1], tan[0] ]
	

def Incremental (l):
	"Algoritmo incremental para o problema do fecho convexo de uma lista de pontos"

	if len (l) == 0: return None

	# crio um fecho c/ um ponto
	fecho = Polygon ([ l[0] ])
	fecho.plot ()
	

	# Como nao posso admitir que os pontos estao em posicao geral,
	# preciso tomar cuidado ate encontrar tres pontos nao colineares
	# :-( 
	length = 1
	k = 0
	hi = l[k].hilight ()
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
			# Ponto nao colinear :) - basta tomar cuidado p/ 
			#   construir o poligono c/ a direcao certa
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
			break

	# Ja tenho um fecho com 3 pontos -> basta "cresce-lo"
	for k in range (k+1, len (l)):
		pts = fecho.pts
		l[k-1].unhilight (hi)
		hi = l[k].hilight ()
		control.thaw_update ()

		tan = vertices_tangentes (fecho, l[k])
		# l[k] esta fora do fecho atual <=> len (tan) == 2
		if len (tan) == 2:
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

