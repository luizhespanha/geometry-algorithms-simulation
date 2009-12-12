#!/usr/bin/env python
"""Implementacao das operacoes graficas em Tk.

Esse modulo nao deve ser usado diretamente. Para isso,
veja geocomp.common.control"""

from math import fabs

master = None
canvas = None

def init_display (master):
	globals()['canvas'] = master.canvas
	globals()['master'] = master

def get_canvas ():
	return canvas

def update ():
	canvas.update ()

def sleep ():
	if master.step_by_step.get ():
		master.tk.wait_variable (master.step)
	else:
		master.tk.after (master.delay.get (), master.tk.quit)
		master.tk.mainloop ()


def plot_disc (x, y, color, r):
	plot_id = canvas.create_oval (canvas.r2cx(x)-r, canvas.r2cy(y)-r, 
					canvas.r2cx(x)+r, canvas.r2cy(y)+r, fill=color)
	return plot_id

def plot_line (x0, y0, x1, y1, color, linewidth):
	lineto_id = canvas.create_line (canvas.r2cx(x0), canvas.r2cy(y0), 
					   canvas.r2cx(x1), canvas.r2cy(y1), 
					   fill=color, width=linewidth)
	return lineto_id

def plot_vert_line (x, color, linewidth):
	lineto_id = canvas.create_line (canvas.r2cx(x), 0, 
					   canvas.r2cx(x), int (canvas['height']), 
					   fill=color, width=linewidth)
	return lineto_id

def plot_horiz_line (y, color, linewidth):
	lineto_id = canvas.create_line (0, canvas.r2cy(y), 
					   int (canvas['width']), canvas.r2cy(y), 
					   fill=color, width=linewidth)
	return lineto_id

def plot_delete (id):
	canvas.delete (id)

def config_canvas (minx, maxx, miny, maxy):
	for item in canvas.find_all ():
		canvas.delete (item)


	Dx = maxx - minx
	Dy = maxy - miny

	if canvas.winfo_width () <= 1 and canvas.winfo_height () <= 1:
		width = int (canvas['width'])
		height = int (canvas['height'])
	else:
		width = canvas.winfo_width ()
		height = canvas.winfo_height ()

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
		#return int ((x - x0) * int (cv['width'])*0.8 / dx + 0.1*int (cv['width']))

	def ry (y, y0 = miny, dy = Dy, height=height):
		return height - int ((y - y0) * height*0.8 / dy + 0.1*height)
		#return int (cv['height']) - int ((y - y0) * int (cv['height'])*0.8 / dy + 0.1*int (cv['height']))

	#print canvas['width'], canvas['height'], canvas['confine']
	#print canvas.winfo_width (), canvas.winfo_height ()
	
	canvas.r2cx = rx
	canvas.r2cy = ry

def hide_algorithm ():
	return master.show_var.get () != 0

