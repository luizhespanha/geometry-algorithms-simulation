#!/usr/bin/env python
"Algoritmo Diametro"

from geocomp.common.segment import Segment
import math
from geocomp.common import control
from geocomp.common.guiprim import *
from geocomp.convexhull.graham import Graham

def Diameter (l):
	"""Algoritmo Diametro para encontrar o par de pontos mais distantes

	Ele consiste de:
	- determinar o fecho convexo dos pontos passados
	- determinar o conjunto de pares antipodas do fecho convexo
	- determinar o par antipoda cujos pontos estao a uma distancia maxima
	"""

	if len (l) < 2: return None
	if len (l) == 2:
		ret = Segment (l[0], l[1])
		ret.extra_info = 'distancia: %.2f'%math.sqrt (dist2 (l[0], l[1]))
		return ret
	
	ch = Graham (l)
	ch.hide ()
	ch.plot (config.COLOR_ALT4)

	control.sleep ()

	pairs = antipodes (ch)
	cores = (config.COLOR_ALT1,)

	#print `pairs`

	i=0
	for p,q in pairs:
		p.hilight (cores[i])
		q.hilight (cores[i])
		p.lineto (q, cores[i])
		i = (i+1) % len (cores)

	control.sleep ()

	farthest = dist2 (pairs[0][0], pairs[0][1])
	a = pairs[0][0]
	b = pairs[0][1]
	hia = a.hilight ()
	hib = b.hilight ()
	id = a.lineto (b)

	for i in range (1, len (pairs)):
		dist = dist2 (pairs[i][0], pairs[i][1])
		if dist > farthest:
			control.freeze_update ()
			a.unhilight (hia)
			b.unhilight (hib)
			control.plot_delete (id)

			farthest = dist
			a = pairs[i][0]
			b = pairs[i][1]

			hia = a.hilight ()
			hib = b.hilight ()
			id = a.lineto (b)
			control.thaw_update ()
	
	ret = Segment (a, b)
	ret.extra_info = 'distancia: %.2f'%math.sqrt (farthest)
	return ret

def antipodes (poly):
	"Determina os pares antipodas de um poligono convexo"
	pairs = []
	v = poly.to_list ()
	n = len (v)
	i = n - 1
	j = 0

	area      = area2 (v[i], v[ (i+1)%n ], v[j])
	area_nova = area2 (v[i], v[ (i+1)%n ], v[ (j+1)%n ])
	while area_nova > area:
		j = (j + 1) % n
		area = area_nova
		area_nova = area2 (v[i], v[ (i+1)%n ], v[ (j+1)%n ])
	
	j0 = j

	while j != 0:
		i = (i + 1) % n
		pairs.append ( (v[i], v[j]) )
		blink (v[i], v[j])

		while area2 (v[i], v[(i+1)%n], v[j]) < \
		      area2 (v[i], v[(i+1)%n], v[(j+1)%n]):
			j = (j + 1) % n
			if j == 0: break

			if i != j0 or j != 0:
				pairs.append ( (v[i], v[j]) )
				blink (v[i], v[j])

		else:
			k = (j+1)%n
			if area2 (v[i], v[(i+1)%n], v[j]) == \
			   area2 (v[i], v[(i+1)%n], v[k]):
				if j != 0:
					if i != j0 or k != 0:
						pairs.append ( (v[i], v[k]) )
						blink (v[i], v[k])

	return pairs

def blink (p, q):
	p.hilight ()
	q.hilight ()
	control.sleep ()
	p.unhilight ()
	q.unhilight ()

