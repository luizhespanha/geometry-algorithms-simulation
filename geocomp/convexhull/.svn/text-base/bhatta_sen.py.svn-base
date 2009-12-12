#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""B. K. Bhattacharya and S. Sen. 
  On a Simple, Practical, Optimal, Output-Sensitive Randomized 
    Planar Convex Hull Algorithm. 
  J. Algorithms, 25:177--193, 1997
 http://citeseer.nj.nec.com/206645.html
"""

from geocomp.common import control
from geocomp.common.polygon import Polygon
from geocomp.common.guiprim import *
from geocomp import config
import random

def inside_restricted (a, b, c, p):
	"""verifica se p esta dentro do triangulo a,b,c
	
	Admite que left (a, b, c) == left (a, b, p) == TRUE
	"""
	if not left_on (b, c, p):
		return 0
	elif not left_on (c, a, p):
		return 0
	return 1

def bhatta_sen_upper_rec (a, b, S):
	"""Constroi a parte superior do fecho convexo"""
	
	# step 1/2/3
	again = 1

	while again:
		if len (S) == 1:
			return [ S[0] ]
		j = int (random.uniform (0, len (S)/2))
		again = 0

		p1 = S[2*j+1]
		p2 = S[2*j]
		p1.hilight ()
		p2.hilight ()
		if inside_restricted (b, a, S[2*j+1], S[2*j]):
			S.remove (S[2*j])
			again = 1
		elif inside_restricted (b, a, S[2*j], S[2*j+1]):
			S.remove (S[2*j+1])
			again = 1

		p1.unhilight ()
		p2.unhilight ()

	
	# step 4
	m = 0
	if left (S[2*j], S[2*j+1], a):
		p1 = S[2*j+1]
		p2 = S[2*j]
	else:
		p1 = S[2*j]
		p2 = S[2*j+1]
	id = p1.lineto (p2, config.COLOR_ALT4)
	area_m = area2 (p1, p2, S[m])
	for i in range (1, len(S)):
		area_i = area2 (p1, p2, S[i])
		if area_i > area_m:
			m = i
			area_m = area_i
	pm = S[m]
	control.plot_delete (id)

	id = pm.hilight (config.COLOR_ALT1)
	control.sleep ()
	
	S1 = []
	S2 = []

	# step 5
	i = j
	#map (lambda p: p.hilight (config.COLOR_ALT2), S)
	#control.sleep ()
	#map (lambda p: p.unhilight (), S)
	control.sleep ()
	cont = []
	for j in range (0, len(S)/2):
		cont.extend ([2*j, 2*j+1])
		if S[2*j].x < S[2*j+1].x:
			p1 = S[2*j]
			p2 = S[2*j+1]
		else:
			p1 = S[2*j+1]
			p2 = S[2*j]

		p1.hilight ()
		p2.hilight (config.COLOR_ALT3)

		if p2.x <= pm.x:
			if left (pm, p2, p1):
				S1.append (p1)
				S1.append (p2)
			else:
				S1.append (p1)
		elif pm.x <= p1.x:
			if left (pm, p1, p2):
				S2.append (p2)
			else:
				S2.append (p1)
				S2.append (p2)
		else: # p1.x < pm.x < p2.x
			control.sleep ()
			S1.append (p1)
			S2.append (p2)

		p1.unhilight ()
		p2.unhilight ()

	pm.unhilight (id)
	if len (S) % 2 == 1:
		S1.append (S[-1])
		S2.append (S[-1])
	control.sleep ()
	
	map (lambda p: p.hilight (), S1)
	control.sleep ()
	
	# step 6
	for p in S1[:]:
		if not left (b, pm, p):
			S1.remove (p)
			p.unhilight ()

	control.sleep ()
	map (lambda p: p.unhilight (), S1)
	control.sleep ()
	map (lambda p: p.hilight (), S2)
	control.sleep ()

	for p in S2[:]:
		if not left (pm, a, p):
			S2.remove (p)
			p.unhilight ()
	control.sleep ()
	map (lambda p: p.unhilight (), S2)

	# step 7
	ret1 = []
	ret2 = []
	if len (S2) != 0:
		id = a.lineto (pm, config.COLOR_ALT4)
		ret2 = bhatta_sen_upper_rec (a, pm, S2)
		a.remove_lineto (pm, id)
		ret2[-1].lineto (pm)
	ret2.append (pm)
	if len (S1) != 0:
		id = pm.lineto (b, config.COLOR_ALT4)
		ret1 = bhatta_sen_upper_rec (pm, b, S1) 
		pm.remove_lineto (b, id)
		pm.lineto (ret1[0])
	
	ret2.extend (ret1)

	return ret2

#ok, eu fiquei com preguiça e simplesmente copiei/colei a funcao 
# abaixo, que e' simetrica `a acima
def bhatta_sen_lower_rec (a, b, S):
	"""Constroi a parte inferior do fecho convexo"""
	
	# step 1
	

	# step 1/2/3
	again = 1

	while again:
		if len (S) == 1:
			return [ S[0] ]
		j = int (random.uniform (0, len (S)/2))
		again = 0

		p1 = S[2*j+1]
		p2 = S[2*j]
		p1.hilight ()
		p2.hilight ()
		if inside_restricted (b, a, S[2*j+1], S[2*j]):
			S.remove (S[2*j])
			again = 1
		elif inside_restricted (b, a, S[2*j], S[2*j+1]):
			S.remove (S[2*j+1])
			again = 1

		p1.unhilight ()
		p2.unhilight ()

	# step 4
	m = 0
	if left (S[2*j], S[2*j+1], a):
		p1 = S[2*j+1]
		p2 = S[2*j]
	else:
		p1 = S[2*j]
		p2 = S[2*j+1]
	id = p1.lineto (p2, config.COLOR_ALT4)
	area_m = area2 (p1, p2, S[m])
	for i in range (1, len(S)):
		area_i = area2 (p1, p2, S[i])
		if area_i > area_m:
			m = i
			area_m = area_i
	pm = S[m]
	control.plot_delete (id)

	id = pm.hilight (config.COLOR_ALT1)
	control.sleep ()
	
	S1 = []
	S2 = []

	# step 5
	i = j
	#map (lambda p: p.hilight (config.COLOR_ALT2), S)
	#control.sleep ()
	#map (lambda p: p.unhilight (), S)
	control.sleep ()
	cont = []
	for j in range (0, len(S)/2):
		cont.extend ([2*j, 2*j+1])
		if S[2*j].x < S[2*j+1].x:
			p1 = S[2*j]
			p2 = S[2*j+1]
		else:
			p1 = S[2*j+1]
			p2 = S[2*j]

		p1.hilight ()
		p2.hilight (config.COLOR_ALT3)

		if p2.x <= pm.x:
			if right (pm, p2, p1):
				S1.append (p1)
				S1.append (p2)
			else:
				S1.append (p1)
		elif pm.x <= p1.x:
			if right (pm, p1, p2):
				S2.append (p2)
			else:
				S2.append (p1)
				S2.append (p2)
		else: # p1.x < pm.x < p2.x
			control.sleep ()
			S1.append (p1)
			S2.append (p2)

		p1.unhilight ()
		p2.unhilight ()

	pm.unhilight (id)
	if len (S) % 2 == 1:
		S1.append (S[-1])
		S2.append (S[-1])
	control.sleep ()
	
	map (lambda p: p.hilight (), S1)
	control.sleep ()
	
	# step 6
	for p in S1[:]:
		if not right (a, pm, p):
			S1.remove (p)
			p.unhilight ()

	control.sleep ()
	map (lambda p: p.unhilight (), S1)
	control.sleep ()
	map (lambda p: p.hilight (), S2)
	control.sleep ()

	for p in S2[:]:
		if not right (pm, b, p):
			S2.remove (p)
			p.unhilight ()
	control.sleep ()
	map (lambda p: p.unhilight (), S2)

	# step 7
	ret1 = []
	ret2 = []
	if len (S1) != 0:
		id = a.lineto (pm, config.COLOR_ALT4)
		ret1 = bhatta_sen_lower_rec (a, pm, S1)
		a.remove_lineto (pm, id)
		ret1[-1].lineto (pm)
	ret1.append (pm)
	if len (S2) != 0:
		id = pm.lineto (b, config.COLOR_ALT4)
		ret2 = bhatta_sen_lower_rec (pm, b, S2) 
		pm.remove_lineto (b, id)
		pm.lineto (ret2[0])
	
	ret1.extend (ret2)

	return ret1

def Bhatta_Sen (l):
	"""Algoritmo otimo proposto por Bhattacharya e Sen para encontrar o fecho convexo de l"""
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
		fecho.append (l[dirs[i]])
		S1 = []
		a = l[dirs[i]]
		b = l[dirs[j]]
		for p in l:
			if right (a, b, p):
				S1.append (p)
		id = a.lineto (b, config.COLOR_ALT4)
		aux = []
		if len (S1) > 0:
			if dirs[i] == south  or  dirs[i] == west:
				aux = bhatta_sen_lower_rec (a, b, S1)
			else:
				aux = bhatta_sen_upper_rec (a, b, S1)
		a.remove_lineto (b, id)
		if len (aux) > 0:
			a.lineto (aux[0])
			aux[-1].lineto (b)
		else:
			a.lineto (b)
		fecho.extend (aux)

	if len (l) == 1:
		fecho = [ l[0] ]
	pol = Polygon (fecho)
	pol.plot ()
	pol.extra_info = "vertices: %d" %len (fecho)

	return pol
