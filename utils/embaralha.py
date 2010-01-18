#!/usr/bin/env python

import random

def embaralha (l):
	for i in range (len (l) -1, -1, -1):
		index = int (random.uniform (0, i+1))
		aux = l[i]
		l[i] = l[index]
		l[index] = aux
	
	return l
