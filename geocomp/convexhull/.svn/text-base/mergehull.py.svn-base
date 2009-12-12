#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Algoritmo Merge Hull"""

from geocomp.common.polygon import Polygon
from geocomp.common import control
from geocomp.common.guiprim import *


def Mergehull (l):
	"""Algoritmo Merge Hull para o problema do Fecho Convexo"""
	if len (l) == 0: return None
	
	def cmp (a, b):
		if a.x < b.x: return -1
		if a.x > b.x: return 1
		if a.y < b.y: return -1
		return a.y > b.y
	
	l.sort (cmp)

	(min_pt, max_pt, hull) = mergehull_rec (l)

	hull.extra_info = 'vertices: %d'%len (hull.to_list ())
	return hull

def mergehull_rec (l):
	"""Funcao recursiva que implementa o Merge Hull

	Retorna os pontos com coordenada x minima e maxima do fecho convexo
	encontrado, alem do proprio fecho.
	"""
	n = len (l)
	if n == 1:
		#l[0].prev = l[0].next = l[0]
		pol = Polygon ( [ l[0] ] )
		pol.plot ()
		#control.sleep ()
		return (l[0], l[0], pol)
	
	# Divisao
	l1 = l[:n/2]
	l2 = l[n/2:]

	id = control.plot_vert_line ((l2[0].x + l1[-1].x) / 2.)
	control.sleep ()

	# Conquista
	ch1 = mergehull_rec (l1)

	ch2 = mergehull_rec (l2)

	v = ch1[1]
	u = ch2[0]

	control.plot_delete (id)

	# Combinar
	sup = superior_tangent (v, u)
	id_sup = sup[0].lineto (sup[1], config.COLOR_ALT1)
	inf = inferior_tangent (v, u)
	id_inf = inf[0].lineto (inf[1], config.COLOR_ALT1)

	control.freeze_update ()
	control.plot_delete (id_sup)
	control.plot_delete (id_inf)
	ch1[2].hide ()
	ch2[2].hide ()

	sup[0].prev = sup[1]
	sup[1].next = sup[0]

	inf[0].next = inf[1]
	inf[1].prev = inf[0]

	ch1[2].pts = inf[0]
	ch1[2].plot ()
	control.thaw_update ()

	return (ch1[0], ch2[1], ch1[2])


def superior_tangent (v, u):
	"""Determina a tangente superior aos poligonos que contem v e u"""
	v.lineto (u, config.COLOR_ALT1)
	hiv = v.hilight ()
	hiu = u.hilight ()

	ch1 = is_sup_tan_ch1 (v, u)
	ch2 = is_sup_tan_ch2 (v, u)
	while not (ch1 and ch2):
		while not ch1:
			v.remove_lineto (u)
			v.unhilight (hiv)

			v = v.next

			hiv = v.hilight ()
			v.lineto (u, config.COLOR_ALT1)
			control.sleep ()
			ch1 = is_sup_tan_ch1 (v, u)

		ch2 = is_sup_tan_ch2 (v, u)
		while not ch2:
			v.remove_lineto (u)
			u.unhilight (hiu)

			u = u.prev

			hiu = u.hilight ()
			v.lineto (u, config.COLOR_ALT1)
			control.sleep ()
			ch2 = is_sup_tan_ch2 (v, u)

		ch1 = is_sup_tan_ch1 (v, u)
	
	v.unhilight (hiv)
	u.unhilight (hiu)
	v.remove_lineto (u)
	return (v, u)

def inferior_tangent (v, u):
	"""Determina a tangente inferior aos poligonos que contem v e u"""
	v.lineto (u, config.COLOR_ALT1)
	hiv = v.hilight (config.COLOR_ALT3)
	hiu = u.hilight (config.COLOR_ALT3)

	ch1 = is_inf_tan_ch1 (v, u)
	ch2 = is_inf_tan_ch2 (v, u)
	while not (ch1 and ch2):
		while not ch1:
			v.remove_lineto (u)
			v.unhilight (hiv)

			v = v.prev

			hiv = v.hilight (config.COLOR_ALT3)
			v.lineto (u, config.COLOR_ALT1)
			control.sleep ()
			ch1 = is_inf_tan_ch1 (v, u)

		ch2 = is_inf_tan_ch2 (v, u)
		while not ch2:
			v.remove_lineto (u)
			u.unhilight (hiu)

			u = u.next

			hiu = u.hilight (config.COLOR_ALT3)
			v.lineto (u, config.COLOR_ALT1)
			control.sleep ()
			ch2 = is_inf_tan_ch2 (v, u)

		ch1 = is_inf_tan_ch1 (v, u)
	
	v.unhilight (hiv)
	u.unhilight (hiu)
	v.remove_lineto (u)
	return (v, u)
	

def is_tan (a, b, c, d, e, f):
	"Funcao generica usada pelas funcoes is_{sup,inf}_tan_ch{1,2}"
	if f (a, b, c): return 1
	if d: return 0
	if not collinear (a, b, c): return 0
	if dist2 (e, c) > dist2 (b, a): return 0
	return 1

def is_sup_tan_ch1 (v, u):
	"Retorna verdadeiro se vu é tangente superior ao poligono que contem v"
	if v == v.next: return 1
	return is_tan (v, u, v.next, v != v.next.next, u, right)

def is_sup_tan_ch2 (v, u):
	"Retorna verdadeiro se vu é tangente superior ao poligono que contem u"
	if u == u.next: return 1
	return is_tan (v, u, u.prev, u != u.prev.prev, v, right)

def is_inf_tan_ch1 (v, u):
	"Retorna verdadeiro se vu é tangente inferior ao poligono que contem v"
	if v == v.next: return 1
	return is_tan (v, u, v.prev, v != v.prev.prev, u, left)

def is_inf_tan_ch2 (v, u):
	"Retorna verdadeiro se vu é tangente inferior ao poligono que contem u"
	if u == u.next: return 1
	return is_tan (v, u, u.next, u != u.next.next, v, left)

