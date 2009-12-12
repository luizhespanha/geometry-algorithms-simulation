#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import math

minx = 0
miny = 0
maxx = 100
maxy = 100

tam_seg = 4
tan_angulo = 0.732050808

num_segs = 200

lista_xs = []
lista_ys = []

for i in range(0,num_segs):
    r1 = random.random()
    while(r1 in lista_xs):
        r1 = random.random()

    x1 = r1 * maxx

    r2 = random.random()
    while(r2 in lista_ys):
        r2 = random.random()

    y1 = r2 * maxy
   
    c = - (tam_seg ** tam_seg / (1 + tan_angulo**2 ) + x1**2)

    x2 = x1 + (math.sqrt(4 * x1**2 - 4 * c) / 2)

#    if x2 < 0:
#        x2 = x1 - (math.sqrt(4 * x1**2 - 4 * c) / 2)

    y2 = y1 + tan_angulo * (x2 - x1)

#    print str(x1) + ',' + str(y1) + ' e o c: ' + str(c) + ' e o outro: ' + str(x2) + ',' + str(y2)

    print str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2)
