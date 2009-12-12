#!/usr/bin/env python
"""Algoritmo forca-bruta"""

from geocomp.common.segment import Segment
from geocomp.common import control
from geocomp.common.guiprim import *
import math


def Brute (l):
	"Algoritmo forca bruta para encontrar o par de pontos mais distante"

	if len (l) < 2: return None
	
	farthest = 0
	a = b = None
	id = None

	for i in range (len(l)):
		for j in range (i + 1, len (l)):
			dist = dist2 (l[i], l[j])
			if dist > farthest:
				control.freeze_update ()
				if a != None: a.unhilight (hia)
				if b != None: b.unhilight (hib)
				if id != None: control.plot_delete (id)

				farthest = dist
				a = l[i]
				b = l[j]

				hia = a.hilight ()
				hib = b.hilight ()
				id = a.lineto (b)
				control.thaw_update ()
				control.update ()
	
	ret = Segment (a, b)
	ret.extra_info = 'distancia: %.2f'%math.sqrt (dist2 (a, b))
	return ret

