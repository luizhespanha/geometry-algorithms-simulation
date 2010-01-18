#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import math

class Point:
	"Um ponto representado por suas coordenadas cartesianas"

	def __init__ (self, x, y, z=None):
		"Para criar um ponto, passe suas coordenadas."
		self.x = x
		self.y = y
		self.z = z
		self.lineto_id = {}

class Segment:
	"Um segmento de reta"
	def __init__ (self, pto_from=None, pto_to=None, intersected=False):
		"Para criar, passe os dois pontos extremos"
		self.init = pto_from
		self.to = pto_to
		self.intersected = False
	
	def __repr__ (self):
		"retorna uma string da forma [ ( x0 y0 );( x1 y1 ) ]"
		return '[ '+`self.init`+'; '+`self.to`+' ]'

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

def intersectaprop(a,b,c,d):
    if collinear(a,b,c) or collinear(a,b,d) or collinear(c,d,a) or collinear(c,d,b): return False
    else: return (left(a,b,c) ^ left(a,b,d)) and (left(c,d,a) ^ left(c,d,b))

def entre(a,b,c):
    if collinear(a,b,c) == False: return False
    if a.x != b.x:
        return a.x <= c.x <= b.x or b.x <= c.x <= a.x
    else:
        return a.y <= c.y <= b.y or b.y <= c.y <= a.y

def inter(segmento1, segmento2): 
    if intersectaprop(segmento1.init, segmento1.to, segmento2.init, segmento2.to): return True
    elif entre(segmento1.init, segmento1.to, segmento2.init) or \
       entre(segmento1.init, segmento1.to, segmento2.to) or \
       entre(segmento2.init, segmento2.to, segmento1.init) or \
       entre(segmento2.init, segmento2.to, segmento1.to):
        return True
    else: return False
    



minx = 0
miny = 0
maxx = 100
maxy = 100

tam_seg = 10
tan_angulo = 0.5

num_segs = 100

lista_xs = []
lista_ys = []
lista_segs = []

while(len(lista_segs) < num_segs):
    x1 = random.randint(0,maxx)
    while(x1 in lista_xs):
        x1 = random.randint(0,maxx)

    y1 = random.randint(0,maxy)
    while(y1 in lista_ys):
        y1 = random.randint(0,maxy)

    lista_xs.append(x1)
    lista_ys.append(y1)

    p1 = Point(x1,y1)

    c =  x1**2 - (tam_seg**2 / (1 + tan_angulo**2 ))

    x2 = x1 + (math.sqrt(4 * x1**2 - 4 * c) / 2)

#    if x2 < 0:
#        x2 = x1 - (math.sqrt(4 * x1**2 - 4 * c) / 2)

    tan = random.uniform(tan_angulo, tan_angulo + 1)

    r = random.random()
    if r >= 0.90:
        y2 = y1 - tan * (x2 - x1)
    else:
        y2 = y1 + tan * (x2 - x1)

    p2 = Point(x2,y2)

    candidato = Segment(p1,p2)
    intersectou = False

    for seg in lista_segs:
        if inter(candidato,seg) == True:
            intersectou = True
            break

    if intersectou == False: 
        print str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2)
        lista_segs.append(candidato)























