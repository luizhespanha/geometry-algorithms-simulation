#!/usr/bin/env python
"""Timothy M. Chan
Optimal Output-Sensitive Convex Hull Algorithms in Two and Three Dimensions
   Discrete & Computational Geometry, volume 16,1996
url = "citeseer.nj.nec.com/article/chan96optimal.html"
"""

from geocomp.common.polygon import Polygon
from geocomp.common import control
from geocomp.common.guiprim import *
from geocomp.convexhull.graham import Graham


def Chan (l):
	n = len (l)
	if n == 0: return None
	if n == 1 or n == 2:
		ret = Polygon (l)
		ret.plot ()
		ret.extra_info = 'vertices: %d'%n
		return ret

	i = 2
	while 1:
		H = min (1<< (1<<i), n)
		m = H
		ch = Hull2D (l, m, H)
		#print ch
		if ch != None: 
			ch.extra_info = 'vertices: %d'%len (ch.to_list ())
			return ch
		i = i + 1

def Hull2D (P, m, H):

	#print m, H
	lines = []
	n = len (P)
	CHs = []
	num = n/m

	a = 0
	while a < n:
		b = min (a+m, n)
		l = P[a:b]
		ids = []
		for p in l: ids.append (p.hilight ())
		ch = Graham (l)
		#ch.hide ()
		for p in P[a:b]: p.unhilight (ids.pop ())
		CHs.append (ch)
		a = b

	i0 = 0
	# encontrando o ponto mais a direita
	p0 = CHs[0].pts
	for ch in CHs:
		for p in ch.to_list ():
			if p.x > p0.x: p0 = p
			elif p.x == p0.x: 
				if p.x > p0.x: p0 = p
	
	fecho = [ p0 ]
	for ch in CHs: ch.hide ()
	#control.sleep (2)
	for k in range (0, H):
		Q = []
		for ch in CHs:
			ch.plot ()
			p = ch.pts
			initial = 1
			while 1:
				direction = area2 (fecho[-1], p, p.next)
				if direction < 0:
					p = p.next
					initial = 0
				elif direction == 0 \
					and dist2 (fecho[-1], p) \
					    < dist2 (fecho[-1], p.next):
					p = p.next
					initial = 0
				elif initial:
					p = p.next
				else:
					Q.append (p)
					p.hilight ()
					control.sleep ()
					ch.pts = p.prev
					ch.hide ()
					break
			

		control.sleep ()
		p = Q[0]
		for q in Q[1:]:
			direction = area2 (fecho[-1], p, q)
			if direction < 0:
				p = q
			elif direction == 0:
				if (dist2 (fecho[-1], p) < dist2 (fecho[-1], q)):
					p = q

		for q in Q: q.unhilight ()
		lines.append (fecho[-1].lineto (p, 'green'))
		fecho.append (p)
		if p == p0: 
			#for ch in CHs: ch.hide ()
			#print 'fecho =',`fecho`
			fecho.pop ()
			for i in lines:
				control.plot_delete (i)
			poly = Polygon (fecho)
			poly.plot ()
			return poly
	
	#for ch in CHs: ch.hide ()
	for i in lines:
		control.plot_delete (i)
	return None
