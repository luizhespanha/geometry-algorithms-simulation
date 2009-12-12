#!/usr/bin/env python

# TODO: 
#     -> fazer sair c/ C-q !!!

import os
import string
from gtk import *
from gnome.ui import *
import geocomp
from geocomp import config
from geocomp.gui import gnome

import sys

class App:
	def __init__ (self):
		self.panel = {}
		self.step_completed = 0
		self.labels = []
		self.ppu = 1.0
		self.idle_id = None

		self.window = GtkWindow ()
		self.window.connect ('destroy', mainquit)
		self.window.set_title ('Geocomp')
		self.window.set_border_width (10)

		self.out_vbox = GtkVBox ()
		self.window.add (self.out_vbox)

		self.extra_label = GtkLabel ('----------')
		self.out_vbox.pack_end (self.extra_label, expand = FALSE)

		self.main_hbox = GtkHBox ()
		self.out_vbox.pack_start (self.main_hbox)

		self.canvas_vbox = GtkVBox ()
		self.main_hbox.pack_end (self.canvas_vbox)

		ha = GtkAdjustment (0, 0, 1000, 40, 100, 100)
		va = GtkAdjustment (0, 0, 1000, 40, 100, 100)
		self.scroll = GtkScrolledWindow (ha, va)
		self.canvas_vbox.pack_start (self.scroll)

		#self.canvas = GnomeCanvas (aa=TRUE)
		self.canvas = GnomeCanvas (aa=FALSE)
		self.canvas.set_usize (config.WIDTH, config.HEIGHT)
		self.canvas.set_scroll_region(0,0, config.WIDTH, config.HEIGHT)
		self.scroll.add (self.canvas)

		self.controls_box = GtkHBox ()
		self.canvas_vbox.pack_end (self.controls_box, expand=FALSE)

		self.dyn_controls_box = GtkHBox ()
		self.controls_box.pack_start (self.dyn_controls_box)

		self.delay = GtkSpinButton (GtkAdjustment (config.DELAY, 0, config.MAX_DELAY, 10, config.MAX_DELAY/10, config.MAX_DELAY/10), digits=0, climb_rate=10)
		self.delay.set_numeric (TRUE)
		self.dyn_controls_box.pack_start (self.delay)#, expand=TRUE, fill=FALSE)

		self.step = GtkCheckButton ('passo a passo')
		self.step.set_state (TRUE)
		self.step.connect_after ('clicked', self.step_clicked)
		self.dyn_controls_box.pack_start (self.step, fill=FALSE)

		self.zoom_in = GtkButton ('+')
		self.zoom_out = GtkButton ('-')
		#self.zoom_box = GtkHBox ()
		#self.canvas_vbox.pack_start (self.zoom_box)
		self.dyn_controls_box.pack_start (self.zoom_in)
		self.dyn_controls_box.pack_start (self.zoom_out)
		self.zoom_in.connect ('clicked', self.zoom, 1.5)
		self.zoom_out.connect ('clicked', self.zoom, 2.0/3.0)

		self.hide = GtkCheckButton ('esconder')
		self.hide.set_state (TRUE)
		self.controls_box.pack_start (self.hide, fill=FALSE)


		geocomp.init_display (gnome, self)


		self.left_box = GtkVBox ()
		self.left_box.set_border_width (5)
		self.main_hbox.pack_start (self.left_box, expand=FALSE)

		self.file_box = GtkVBox ()
		self.left_box.pack_start (self.file_box)

		self.files_combo = GtkCombo ()
		self.handler_id = self.files_combo.entry.connect ("changed", self.open_file)
		#self.handler_id = self.files_combo.list.connect ("selection_changed", self.open_file)
		self.files_combo.set_value_in_list (val = TRUE, ok_if_empty = FALSE)
		self.files_combo.disable_activate ()
		self.files_combo.entry.set_editable (FALSE)
		self.file_box.pack_start (self.files_combo, expand = FALSE)

		self.create_buttons (None, (geocomp, None))

		
		self.window.show_all ()

		style = self.canvas.get_style ()
		style.bg[STATE_NORMAL] = style.black

		self.update_files (config.DATADIR, 1)

		self.files_combo.entry.emit ("changed")
		self.window.add_events (GDK.KEY_RELEASE)
#		while events_pending (): mainiteration ()
	

	def zoom (self, clicked, inout):
		self.ppu = self.ppu * inout
		if self.ppu < 1.0: self.ppu = 1.0
		self.canvas.set_pixels_per_unit (self.ppu)
		self.canvas.grab_focus ()

	def update_files (self, directory, init=0):
		"Atualiza a lista de arquivos disponiveis"
		if self.idle_id is not None:
			idle_remove (self.idle_id)
			self.idle_id = None

		files = os.listdir (directory)
		files = filter (lambda x: x[0] != '.', files)
		files.sort ()
		#files.insert (0, '..')
		files.append ('..')
		for i in range (len(files)):
			if os.path.isdir (os.path.join (directory, files[i])):
				files[i] = files[i] + '/'

		self.datadir = directory
		self.files_combo.entry.signal_handler_block (self.handler_id)
		self.files_combo.set_popdown_strings (files)
		self.files_combo.entry.signal_handler_unblock (self.handler_id)

		if not init:
			self.files_combo.entry.signal_handler_block (self.handler_id)
			self.files_combo.entry.set_text (self.cur_file)
			self.files_combo.entry.signal_handler_unblock (self.handler_id)

	def open_file (self, entry):
		selection = os.path.join (self.datadir, entry.get_text ())
		if os.path.isdir (selection):
			if self.idle_id == None:
				self.idle_id = idle_add (self.update_files,
								selection)
		else:
			self.cur_file = os.path.basename (selection)
			self.points = geocomp.open_file (selection)
			geocomp.config_canvas (self.points)
			for l in self.labels:
				l.set_text ('------')
			self.extra_label.set_text ('----------')

	def create_buttons (self, clicked=None, list=None):
		problem = list[0]
		parent = list[1]

		if self.panel.has_key (problem):
			self.buttons.hide ()
			self.buttons = self.panel[problem]
			self.buttons.show_all ()
			self.buttons.focus.grab_focus ()
			return

		if hasattr (self, 'buttons'):
			self.buttons.hide ()

		children = getattr (problem, 'children')
		buttons = GtkTable (len (children), 3, FALSE)
		self.left_box.pack_end (buttons, expand = FALSE)
		row = 0
		first = 1
		for a in children:
			b = GtkButton (a[-1])

			if a[1] == None:  # sub-modulo
				buttons.attach (b, 0, 3, row, row+1, yoptions = 0, ypadding = 1)
				sub_prob = getattr (problem, a[0])
				b.connect ('clicked', self.create_buttons, (sub_prob, problem))
			else:
				buttons.attach (b, 0, 2, row, row+1, yoptions = 0, ypadding = 1)
				alg = getattr (problem, a[0])
				func = getattr (alg, a[1])
				l = GtkLabel ('------')
				buttons.attach (l, 2, 3, row, row+1, yoptions = 0, ypadding = 1)
				b.connect ('clicked', self.run_algorithm, (func, l))
				self.labels.append (l)

			row = row + 1
			if first: 
				b.grab_focus ()
				first = 0
				buttons.focus = b
		if parent != None:
			b = GtkButton ('Voltar')
			b.connect ('clicked', self.create_buttons, (parent, parent))
			buttons.attach (b, 0, 3, row, row+1, yoptions = 0, ypadding = 3)
		else:
			b = GtkButton ('Sair')
			b.connect ('clicked', mainquit)
			buttons.attach (b, 0, 3, row, row+1, yoptions = 0, ypadding = 3)
		self.panel[problem] = buttons
		self.buttons = buttons
		self.buttons.show_all ()

		return
	
	def step_clicked (self, widget):
		self.canvas.grab_focus ()
		self.window.grab_focus ()
		self.step_completed = 1

	def key_release (self, widget, event):
		#print event
		if event.keyval == GDK.space:
			self.step_completed = 1

	def run_algorithm (self, clicked, arg):
		alg = arg[0]
		label = arg[1]

		# desativando os controles que nao fazem sentido durante
		# o algoritmo
		self.left_box.set_sensitive (FALSE)
		if self.hide.get_active ():
			self.dyn_controls_box.set_sensitive (FALSE)
		self.hide.set_sensitive (FALSE)

		self.extra_label.set_text ('----------')
		self.canvas.grab_focus ()
		id = self.window.connect ('key_release_event', self.key_release)
		while events_pending (): mainiteration ()

		cont, extra_info = geocomp.run_algorithm (alg, self.points)

		self.window.disconnect (id)
		if self.hide.get_active ():
			self.dyn_controls_box.set_sensitive (TRUE)
		self.hide.set_sensitive (TRUE)
		self.left_box.set_sensitive (TRUE)
		label.set_text ("%6d"%cont)
		if extra_info is not None:
			self.extra_label.set_text (extra_info)

if __name__ == '__main__':

	app = App ()

	mainloop ()

