#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import math

minx = 0
miny = 0
maxx = 1000
maxy = 1000

tam_seg = 10

num_segs = 12

lista_segs = []

x1,y1,x2,y2 = 0,0,maxx,0

while(len(lista_segs) < num_segs):
    y1 = y1 + ( float(maxx) / num_segs)    
    y2 = y1 
  
    print str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2)

    lista_segs.append(1)





