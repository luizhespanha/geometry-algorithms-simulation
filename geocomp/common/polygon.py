#!/usr/bin/env python

import control
from geocomp import config

class Polygon:
	"""Um Poligono. Implementado como uma lista ligada de pontos"""
	def __init__ (self, pontos):
		"Para criar o poligono, passe uma lista (de python) de pontos"
		self.cid = {}
		self.hid = {}
		self.hidp = {}

		p = self.pts = pontos[0]

		for i in range (1, len (pontos)):
			p.next = pontos[i]
			pontos[i].prev = p
			p = p.next

		p.next = self.pts
		self.pts.prev = p
			
	def __repr__ (self):
		"Retorna uma string da forma [ ( x0 y0 ) ( x1 y1 ) ... ]"
		ret = '[ '
		p = self.pts
		while p.next != self.pts:
			ret = ret + `p` + ' '
			p = p.next
		ret = ret + `p`
		ret = ret + ' ]'
		return ret
		

	def hilight (self, color_line = config.COLOR_HI_POLYGON, color_point = config.COLOR_HI_POLYGON_POINT):
		"Desenha o poligono com destaque na tela"
		p = self.pts
		while p.next != self.pts:
			self.hid[p] = p.lineto (p.next, color_line)
			self.hidp[p] = p.hilight (color_point)
			p = p.next
		self.hid[p] = p.lineto (p.next, color_line)
		self.hidp[p] = p.hilight (color_point)
		control.update ()

	def plot (self, color = config.COLOR_POLYGON):
		"Desenha o poligono na tela"
		p = self.pts
		while p.next != self.pts:
			self.cid[p] = p.lineto (p.next, color)
			p = p.next
		self.cid[p] = p.lineto (p.next, color)
		control.update ()

	
	def hide (self):
		"Apaga o poligono na tela"
		p = self.pts
		while p.next != self.pts:
			if self.cid.has_key (p):
				control.plot_delete (self.cid[p])
				del (self.cid[p])
			p = p.next

		if self.cid.has_key (p):
			control.plot_delete (self.cid[p])
			del (self.cid[p])
		control.update ()
	
	def to_list (self):
		"Retorna uma lista (de python) com todos os pontos"
		l = []
		p = self.pts
		while p.next != self.pts:
			l.append (p)
			p = p.next
		l.append (p)
		return l
