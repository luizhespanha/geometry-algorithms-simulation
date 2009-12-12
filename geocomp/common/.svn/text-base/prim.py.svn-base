#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Primitivas geometricas usadas nos algoritmos

Use o modulo geocomp.common.guiprim para que essas primitivas sejam
desenhadas na tela à medida que elas são usadas. Também é possível
desenhá-las de um jeito específico para um determinado algoritmo.
Veja geocomp.convexhull.quickhull para um exemplo.
"""

# Numero de vezes que a funcao area2 foi chamada
num_area2 = 0
# Numero de vezes que a funcao dist2 foi chamada
num_dist = 0

def area2 (a, b, c):
	"Retorna duas vezes a área do triângulo determinado por a, b, c"
	global num_area2
	num_area2 = num_area2 + 1
	return (b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)

def left (a, b, c):
	"Verdadeiro se c está à esquerda do segmento orientado ab"
	return area2 (a, b, c) > 0

def left_on (a, b, c):
	"Verdadeiro se c está à esquerda ou sobre o segmento orientado ab"
	return area2 (a, b, c) >= 0

def collinear (a, b, c):
	"Verdadeiro se a, b, c sao colineares"
	return area2 (a, b, c) == 0

def right (a, b, c):
	"Verdadeiro se c está à direita do segmento orientado ab"
	return not (left_on (a, b, c))

def right_on (a, b, c):
	"Verdadeiro se c está à direita ou sobre o segmento orientado ab"
	return not (left (a, b, c))

def dist2 (a, b):
	"Retorna o quadrado da distancia entre os pontos a e b"
	global num_dist
	num_dist = num_dist + 1
	dy = b.y - a.y
	dx = b.x - a.x

	return dy*dy + dx*dx

def entre(a,b,c):
    if collinear(a,b,c) == False: return False
    if a.x != b.x:
        return a.x <= c.x <= b.x or b.x <= c.x <= a.x
    else:
        return a.y <= c.y <= b.y or b.y <= c.y <= a.y

def intersectaprop(a,b,c,d):
    if collinear(a,b,c) or collinear(a,b,d) or collinear(c,d,a) or collinear(c,d,b): return False
    else: return (left(a,b,c) ^ left(a,b,d)) and (left(c,d,a) ^ left(c,d,b))

def inter(segmento1, segmento2): 
    if intersectaprop(segmento1.init, segmento1.to, segmento2.init, segmento2.to): return True
    elif entre(segmento1.init, segmento1.to, segmento2.init) or \
       entre(segmento1.init, segmento1.to, segmento2.to) or \
       entre(segmento2.init, segmento2.to, segmento1.init) or \
       entre(segmento2.init, segmento2.to, segmento1.to):
        return True
    else: return False

def get_count ():
	"Retorna o numero total de operacoes primitivas realizadas"
	return num_area2 + num_dist

def reset_count ():
	"Zera os contadores de operacoes primitivas"
	global num_area2, num_dist
	num_area2 = 0
	num_dist = 0
