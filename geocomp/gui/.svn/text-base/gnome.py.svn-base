#!/usr/bin/env python
"""Implementacao das operacoes graficas usando GNOME.

Esse modulo nao deve ser usado diretamente.
Veja geocomp.common.control"""

from gtk import *
from math import fabs

master = None
canvas = None

def init_display (app):
	global canvas, master
	master = app
	canvas = master.canvas
	canvas.items = []

def get_canvas ():
	return canvas

def update ():
	while events_pending (): 
		mainiteration ()

def sleep ():
	if master.step.get_active ():
		master.step_completed = 0
		while master.step_completed == 0:
			delay = 50
			timeout_add (delay, mainquit)
			mainloop ()
	else:
		delay = master.delay.get_value_as_int ()
		timeout_add (delay, mainquit)
		mainloop ()

def plot_disc (x, y, color, r):
	widget = canvas.root().add ('ellipse', x1=canvas.r2cx(x)-r, y1=canvas.r2cy(y)-r,
					x2=canvas.r2cx(x)+r,y2=canvas.r2cy(y)+r, fill_color=color)
	widget.show ()
	return widget

def plot_line (x0, y0, x1, y1, color, linewidth):
	widget = canvas.root().add ('line', points=(canvas.r2cx(x0), canvas.r2cy(y0), 
							canvas.r2cx(x1), canvas.r2cy(y1)),
					   fill_color=color, width_pixels=linewidth)
	widget.show ()
	return widget

def plot_vert_line (x, color, linewidth):
	widget = canvas.root().add ('line', points=(canvas.r2cx(x), 0, 
					   		canvas.r2cx(x), int (canvas['height'])),
					  fill_color=color, width_pixels=linewidth)
	widget.show ()
	return widget

def plot_horiz_line (y, color, linewidth):
	widget = canvas.root().add ('line', points=(0, canvas.r2cy(y), 
					   		canvas.r2cy(y), int (canvas['height'])), 
					   fill_color=color, width_pixels=linewidth)
	widget.show ()
	return widget

def plot_delete (widget):
	if widget == None: return
	widget.destroy ()

def config_canvas (minx, maxx, miny, maxy):
	for item in canvas.root ().children ():
		item.destroy ()

	Dx = maxx - minx
	Dy = maxy - miny

	alloc = canvas.get_allocation ()
	width = alloc[2]
	height = alloc[3]

	canvas.set_scroll_region(0,0, width, height)

	ratio = float (width)/ float (height)
	ratio_dxdy = float (Dx)/ float (Dy)

	if ratio != ratio_dxdy:
		if ratio_dxdy < ratio:
			new_dx = Dy * ratio
			minx = minx - fabs (Dx-new_dx)/2
			Dx = new_dx
		else:
			new_dy = Dx / ratio
			miny = miny - fabs (Dy-new_dy)/2
			Dy = new_dy


	def rx (x, x0 = minx, dx = Dx, width=width):
		return int ((x - x0) * width*0.8 / dx + 0.1*width)

	def ry (y, y0 = miny, dy = Dy, height=height):
		return height - int ((y - y0) * height*0.8 / dy + 0.1*height)
	
	canvas.r2cx = rx
	canvas.r2cy = ry

def hide_algorithm ():
	return master.hide.get_active () != FALSE
