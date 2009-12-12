#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Algoritmo Quick Hull"""

from geocomp.common.polygon import Polygon
from geocomp.common import control
from geocomp.common import prim
from geocomp import config


def triang (a, b, c):
	"desenha  (e apaga) os lados do triangulo abc"
	a.lineto (c, config.COLOR_PRIM)
	#b.lineto (a, config.COLOR_PRIM)
	c.lineto (b, config.COLOR_PRIM)
	c.hilight ()
	control.thaw_update ()
	control.update ()
	control.freeze_update ()

	control.sleep ()

	c.unhilight ()
	a.remove_lineto (c)
	#b.remove_lineto (a)
	c.remove_lineto (b)

def dist2 (a, b):
	"retorna o quadrado da distancia entre a e b"
	return prim.dist2(a, b)

def area2 (a, b, c):
	"retorna duas vezes a area do triangulo abc"
	ret = prim.area2 (a, b, c)
	triang (a, b, c)
	return ret

def left (a, b, c):
	"retorna verdadeiro se c esta a esquerda do segmento ab"
	ret = prim.left (a, b, c)
	triang (a, b, c)
	return ret

def right (a, b, c):
	"retorna verdadeiro se c esta a direita do segmento ab"
	ret = prim.right (a, b, c)
	triang (a, b, c)
	return ret

def collinear (a, b, c):
	"retorna verdadeiro se a, b, c sao colineares"
	ret = prim.collinear (a, b, c)
	#triang (a, b, c)
	return ret

def quickhull_rec (a, b, S):
	"""Constroi o fecho de a ate b. 
	
	Todos os pontos de S estao à direita de ab
	"""
	
	if len (S) == 0:
		a.lineto (b)
		return [a]
	
	j = 0
	area_j = area2 (b, a, S[j])
	for i in range (1, len(S)):
		area_i = area2 (b, a, S[i])
		if area_i > area_j:
			j = i
			area_j = area_i
	
	c = S[j]

	S1 = []
	S2 = []

	lado_a = left (b, c, a)
	lado_b = left (a, c, b)

	id = a.lineto (c, config.COLOR_ALT5)
	for i in range (0, len (S)):
		if right (a, c, S[i]):
			S1.append (S[i])
	a.remove_lineto (c, id)
	id = a.lineto (c, config.COLOR_ALT4)
	fecho = quickhull_rec (a, c, S1)

	a.remove_lineto (c, id)
	id = c.lineto (b, config.COLOR_ALT5)
	for i in range (0, len (S)):
		if right (c, b, S[i]):
			S2.append (S[i])
	c.remove_lineto (b, id)
	
	id = c.lineto (b, config.COLOR_ALT4)
	fecho.extend (quickhull_rec (c, b, S2))
	c.remove_lineto (b, id)

	return fecho

def Quickhull (l):
	"Algoritmo Quick Hull para achar o fecho convexo da lista de pontos l"

	south = north = east = west = 0
	# encontrando o ponto mais baixo
	for i in range (1, len(l)):
		if l[i].y < l[south].y:
			south = i
		elif l[i].y == l[south].y:
			if l[i].x > l[south].x:
				south = i
	
		if l[i].y > l[north].y:
			north = i
		elif l[i].y == l[north].y:
			if l[i].x > l[north].x:
				north = i
	
		if l[i].x < l[west].x:
			west = i
		elif l[i].x == l[west].x:
			if l[i].y > l[west].y:
				west = i

		if l[i].x > l[east].x:
			east = i
		elif l[i].x == l[east].x:
			if l[i].y > l[east].y:
				east = i

	fecho = []
	dirs = [ south, east, north, west ]
	for i in range (0, len (dirs)):
		j = (i+1) % 4
		if dirs[i] == dirs[j]:
			continue
		S1 = []
		a = l[dirs[i]]
		b = l[dirs[j]]
		id = a.lineto (b, config.COLOR_ALT5)
		for p in l:
			if right (a, b, p):
				S1.append (p)
		a.remove_lineto (b, id)
		id = a.lineto (b, config.COLOR_ALT4)
		aux = quickhull_rec (a, b, S1)
		a.remove_lineto (b, id)
		fecho.extend (aux)


	if len (l) == 1:
		fecho = [ l[0] ]
	hull = Polygon (fecho)
	hull.extra_info = 'vertices: %d'%len (hull.to_list ())
	return hull

