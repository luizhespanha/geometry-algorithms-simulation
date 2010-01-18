#!/usr/bin/env python

from Tkinter import *
import geocomp
from geocomp.gui import tk
from geocomp import config
import os
import string

class App:
	def __init__ (self):
		"cria a janela e inicializa tudo"
		self.panel = {}
		self.labels = []
		self.file_cont = 0
		self.current_algorithm = None

		self.tk = Tk ()
		self.tk.title ('Geocomp')
		self.tk.bind ('<Control-q>', self.delete_cb)


		self.bottom_label = Label (self.tk, text = '----------')
		self.bottom_label.pack (side = BOTTOM, fill = X)

		self.left = Frame (self.tk, borderwidth = 10)
		self.left.pack (side = LEFT, fill=Y)

		self.file_frame = Frame (self.left)
		self.file_frame.pack (fill = X)
		self.selected_file = StringVar ()
		self.file_label = Label (self.file_frame, text = 'Arquivo:')
		self.file_label.pack ()
		self.file_sub_frame = Frame (self.file_frame)
		self.file_sub_frame.pack (fill = BOTH)
		self.selected_file.trace_variable ("w", 
				lambda x, y, z, self=self: self.open_file ())

		filename = self.update_files (config.DATADIR)

		self.create_buttons (None, 1)

		self.main_frame = Frame (self.tk)
		self.main_frame.pack (fill=BOTH, expand = 1)
		self.main_frame.bind ('<Control-q>', 
				      lambda event, self=self: self.tk.quit ())

		self.canvas = Canvas (self.main_frame, 
					width = config.WIDTH, 
					height = config.HEIGHT, 
					bg = 'black', 
					takefocus=1)
		self.canvas.pack (fill = BOTH, expand=1)


		self.controls = Frame (self.main_frame)
		self.controls.pack (fill = BOTH, expand = 1)

		self.step_by_step = IntVar ()
		self.step_button = Checkbutton (self.controls, 
						text = 'passo a passo', 
						variable = self.step_by_step)

		self.step_button.grid (row=0, column=0, sticky=W+E, padx=20)

		self.print_canvas = Button (self.controls, 
						text = 'imprimir', 
						command = self.print_to_file)
		self.print_canvas.grid (row=0, column = 1, sticky=W+E, padx=20)

		self.show_var = IntVar ()
		self.show_button = Checkbutton (self.controls, 
						text = 'esconder',
						variable = self.show_var)
		self.show_button.grid (row=0, column = 2, sticky=W+E, padx=20)


		self.delay = Scale (self.main_frame, orient = HORIZONTAL, 
					from_ = 0, to = config.MAX_DELAY, 
					resolution = 10)
		self.delay.set (config.DELAY)
		self.delay.pack (fill = X, side=BOTTOM)

		geocomp.init_display (tk, self)
		self.input = []
		self.step = IntVar ()
		self.step.set (1)
		self.selected_file.set (filename)
		self.tk.protocol ("WM_DELETE_WINDOW", self.delete_cb)

	def update_files (self, directory):
		"Atualiza a lista de arquivos disponiveis"
		if hasattr (self, 'filelist'):
			if self.filelist is not None:
				self.filelist.destroy ()

		files = os.listdir (directory)
		files = filter (lambda x: x[0] != '.', files)
		files.sort ()
		files.insert (0, '..')
		for i in range (len(files)):
			if os.path.isdir (os.path.join (directory, files[i])):
				files[i] = files[i] + '/'

		self.filelist = apply (OptionMenu, 
			(self.file_frame, self.selected_file) + tuple (files))
		self.filelist.pack (fill=X)
		self.filelist['takefocus'] = 1
		self.filelist.directory = directory
		for f in files:
			if os.path.isfile (os.path.join (directory, f)):
				return f
		return '.'

	def delete_cb (self, arg=None):
		""" fechar tudo """
		self.step.set (1)
		self.tk.destroy ()

	def step_cb (self, event):
		"""passo completado"""
		self.step.set (1)
		return 'break'

	def create_buttons (self, clicked, initial = None):
		"""cria botoes p/ algoritmos e problemas"""
		if initial:
			problem = geocomp
			parent = None
		else:
			problem = clicked.problem
			parent = clicked.parent

		if self.panel.has_key (problem):
			self.buttons.pack_forget ()
			self.buttons = self.panel[problem]
			self.buttons.pack (fill = BOTH, side = BOTTOM)
			self.buttons.focus.focus_set ()
			return

		if hasattr (self, 'buttons'):
			self.buttons.pack_forget ()

		children = getattr (problem, 'children')
		buttons = Frame (self.left)
		buttons.pack (fill = BOTH, side = BOTTOM)
		row = 0
		first = 1
		for a in children:
			b = Button (buttons, text = a[-1])
			if a[1] == None:
				b['command'] = lambda self=self, b=b: \
						self.create_buttons (b)
				b.problem = getattr (problem, a[0])
				b.parent = problem
				b.grid (row = row, column = 0, 
					columnspan = 2, sticky = W+E)
			else:
				alg = getattr (problem, a[0])
				func = getattr (alg, a[1])
				alg_name = a[1]
				b['command'] = lambda self=self, func=func,\
					alg_name=alg_name, b=b: \
					self.run_algorithm (func, b, alg_name)
				b.grid (row = row, column = 0, sticky = W+E)
				l = Label (buttons, text = '------')
				l.grid (row = row, column=1, sticky = W+E)
				self.labels.append (l)
				b.label = l

			row = row + 1
			if first: 
				b.focus_set ()
				first = 0
				buttons.focus = b

		if parent != None:
			b = Button (buttons, text = 'Voltar')
			b['command'] = lambda b=b, self=self: self.create_buttons (b)
			b.problem = parent
			b.parent = parent
			b.grid (row = row, column = 0, columnspan = 1, 
				sticky = W+E)
		else:
			b = Button (buttons, text = 'Sair')
			b['command'] = self.delete_cb
			b.grid (row = row, column = 0, columnspan = 2,
				sticky = W+E)

		self.panel[problem] = buttons
		self.buttons = buttons

		return

	def open_file (self, event=None):
		"abre um arquivo de entrada"
		#if self.in_algorithm: return
		selection = os.path.join (self.filelist.directory, 
						self.selected_file.get ())
		if os.path.isdir (selection):
			self.update_files (selection)
			return
		else:
			self.input = geocomp.open_file (selection)
			self.current_filename = self.selected_file.get ()
			geocomp.config_canvas (self.input)
			self.reset_labels ()
			self.current_algorithm = None

	def set_entry (self, var, y, mode):
		"""um item foi selecionado -> atualiza a entry"""
		self.file_entry.delete (0, END)
		self.file_entry.insert (END, self.selected_file.get ())

	def disable (self):
		"""desativa maior parte dos botoes

		(tenta) impedir que outro algoritmo seja iniciado concorrentemente"""
		#self.main_frame.grab_set ()
		#self.left['takefocus'] = 0
		self.filelist['state'] = DISABLED
		self.filelist['takefocus'] = 0
 		for b in self.buttons.children.values () :
 			b['state'] = DISABLED
		if self.show_var.get ():
			self.delay['state'] = DISABLED
			self.step_button['state'] = DISABLED
			self.print_canvas['state'] = DISABLED
		self.show_button['state'] = DISABLED


	def enable (self):
		"""reativa maior parte dos botoes"""
		#self.main_frame.grab_release ()
		#self.left['takefocus'] = 1
		self.filelist['state'] = NORMAL
		self.filelist['takefocus'] = 1
 		for b in self.buttons.children.values () :
 			b['state'] = NORMAL
		if self.show_var.get ():
			self.delay['state'] = NORMAL
			self.step_button['state'] = NORMAL
			self.print_canvas['state'] = NORMAL
		self.show_button['state'] = NORMAL
	
	def reset_labels (self):
		"Joga fora o conteudo de todos os labels"
		for l in self.labels:
			l['text'] = '------'

		self.bottom_label['text'] = '----------'
	
	def print_to_file (self):
		"Imprime self.canvas para um arquivo .eps"
		if self.current_algorithm != None:
			epsfile = self.current_filename + '-' + \
				self.current_algorithm + '-' + \
				`self.file_cont` + '.eps'
		else:
			epsfile = self.current_filename + '-' + \
				`self.file_cont` + '.eps'
		self.canvas.postscript (file=epsfile)
		self.file_cont = self.file_cont + 1
		
	
	def run_algorithm (self, alg, widget, alg_name):
		"""roda o algoritmo alg"""
		self.file_cont = 0
		self.current_algorithm = alg_name

		if len (self.input) == 0:
			return

		self.bottom_label['text'] = '----------'
		self.disable ()
		self.canvas.focus_set ()
		self.tk.bind ('<space>', self.step_cb)

		cont, extra = geocomp.run_algorithm (alg, self.input)

		widget.label['text'] = "%6d"%cont
		if extra is not None:
			self.bottom_label['text'] = extra

		self.tk.unbind ('<space>')
		self.enable ()
			

app = App ()

app.tk.mainloop ()
