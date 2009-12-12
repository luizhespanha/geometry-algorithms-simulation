#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Controla a visualizacao dos algoritmos"""

import time
from geocomp import config

dont_update = 0
dont_sleep = 0
skip = 0
gui = None

def freeze_update (amount = 1):
	"""Impede a atualizacao da tela.

	Junto com thaw_update permite reduzir a quantidade de flicker
	quando um segmento de reta é desenhado e apagado muitas vezes
	em seguida"""
	global dont_update
	dont_update = dont_update + amount

def thaw_update (amount = 1):
	"""Permite a atualizacao da tela.

	Junto com freeze_update permite reduzir a quantidade de flicker
	quando um segmento de reta é desenhado e apagado muitas vezes
	em seguida"""
	global dont_update
	dont_update = dont_update - amount
	if dont_update <= 0:
		dont_update = 0
		update ()

def update ():
	"Atualiza a tela"
	if skip: return
	if dont_update == 0: gui.update ()

# hmm.. acho que eu nao uso as duas proximas funcoes em nenhum lugar...
def freeze_sleep ():
	"""Nao permite que o programa durma entre os passos do algoritmo
	
	Veja thaw_sleep"""
	global dont_sleep
	dont_sleep = dont_sleep + 1

def thaw_sleep ():
	"""Volta a permitir que o programa durma entre os passos do algoritmo

	Veja freeze_sleep"""
	global dont_sleep
	dont_sleep = dont_sleep - 1
	if dont_sleep < 0:
		dont_sleep = 0

def sleep (amount = None):
	"Dorme uma pequena quantia de tempo para que o algoritmo pareca mais lento"
	if skip: return
	# para ajudar a debuggar, se um argumento foi passado, 
	# dormimos a qtde de tempo especificada
	if amount != None:
		time.sleep (amount)
	if dont_sleep == 0:
		gui.sleep ()


def plot_disc (x, y, color, r):
	"""desenha um disco de centro (x,y), raio r e cor color na tela"""
	if skip: return 0
	plot_id = gui.plot_disc (x, y, color, r)
	update ()
	return plot_id

def plot_line (x0, y0, x1, y1, color=config.COLOR_LINE, linewidth = config.LINEWIDTH):
	"""desenha uma linha que vai de (x0,y0) até (x1,y1) de cor color"""
	if skip: return 0
	plot_id = gui.plot_line (x0, y0, x1, y1, color, linewidth)
	update ()
	return plot_id

def plot_vert_line (x, color=config.COLOR_LINE_SPECIAL,
			linewidth=config.LINEWIDTH_SPECIAL):
	"""desenha uma linha vertical passando por x, de cor color"""
	if skip: return 0
	plot_id = gui.plot_vert_line (x, color, linewidth)
	update ()
	return plot_id

# hmm... eu nao uso isso em lugar algum => nao foi testado...
def plot_horiz_line (y, color=config.COLOR_LINE_SPECIAL,
			linewidth=config.LINEWIDTH_SPECIAL):
	"""desenha uma linha horizontal passando por y, de cor color"""
	if skip: return 0
	plot_id = gui.plot_horiz_line (y, color, linewidth)
	update ()
	return plot_id

def plot_delete (id):
	"""apaga da tela o elemento com identificador id"""
	if skip: return 0
	gui.plot_delete (id)
	update ()

def set_gui (toolkit):
	"Funcao interna, para configurar qual o toolkit usado"
	global gui
	gui = toolkit

def set_skip (val):
	"Funcao interna, para (des)ativar as funcoes graficas"
	global skip
	skip = val
