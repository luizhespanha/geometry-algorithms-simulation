#!/usr/bin/env python
"""Contem as mesmas funcoes do modulo geocomp.common.prim, mas desenhando na tela"""

import control
import prim
from geocomp import config


def triang (a, b, c):
	"desenha  (e apaga) os lados do triangulo abc"
	a.lineto (c, config.COLOR_PRIM)
	b.lineto (a, config.COLOR_PRIM)
	c.lineto (b, config.COLOR_PRIM)
	control.thaw_update ()
	control.update ()
	control.freeze_update ()

	control.sleep ()

	a.remove_lineto (c)
	b.remove_lineto (a)
	c.remove_lineto (b)

def dist2 (a, b): 
	"retorna o quadrado da distancia entre a e b"
	ida = a.hilight (config.COLOR_PRIM)
	idb = b.hilight (config.COLOR_PRIM)
	a.lineto (b, config.COLOR_PRIM)
	control.thaw_update ()
	control.update ()
	control.freeze_update ()

	control.sleep ()

	a.remove_lineto (b)
	a.unhilight (ida)
	b.unhilight (idb)

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

def left_on (a, b, c):
	"retorna verdadeiro se c esta a esquerda ou sobre o segmento ab"
	return not right (a, b, c)

def right_on (a, b, c):
	"retorna verdadeiro se c esta a direita ou sobre o segmento ab"
	return not left (a, b, c)

def collinear (a, b, c):
	"retorna verdadeiro se a, b, c sao colineares"
	ret = prim.collinear (a, b, c)
	triang (a, b, c)
	return ret

