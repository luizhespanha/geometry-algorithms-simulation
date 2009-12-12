#!/usr/bin/env python

import sys
import time
import os.path
from string import split, rfind
import geocomp
from geocomp import config
from geocomp.gui import dummy

def get_func (str):

	list = split (str, '/')
	if list[0] == 'geocomp':
		list.pop (0)

	last = list.pop ()
	#ext = last.rfind ('.py', -4)
	ext = rfind (last, '.py', -4)
	if ext != -1: 
		last = last[:ext]

	mod = geocomp
	for name in list:
		mod = getattr (mod, name)

	tuple = (filter (lambda x, last=last: x[0] == last, mod.children))[0]

	if tuple[1] == None: return None

	mod = getattr (mod, last)
	func = getattr (mod, tuple[1])

	return func

def run_alg (func, input):
	init = time.clock ()
	cont, extra = geocomp.run_algorithm (func, input)
	end = time.clock ()

	delta = end - init

	print `cont`, '  ','%.2f'%delta,'s', '  ', extra
	sys.stdout.flush ()

def many_algs (strings):
	filename = strings.pop (0)
	print filename, ':'
	input = geocomp.open_file (filename)

	for func_name in strings:
		print os.path.basename (func_name),':',
		func = get_func (func_name)

		run_alg (func, input)

def many_files (strings):
	func_name = strings.pop (0)
	print func_name,':'
	func = get_func (func_name)

	for filename in strings:
		print os.path.basename (filename),':',
		input = geocomp.open_file (filename)

		run_alg (func, input)


if __name__ == '__main__':
	if len (sys.argv) < 2:
		print sys.argv[0], '<algorithm> <file1> [file2]...'
		print sys.argv[0], '-a <file1> <algorithm1> [algorithm2]...'
		sys.exit (1)

	geocomp.init_display (dummy, None)

	if sys.argv[1] == '-a':
		sys.argv.pop (0)
		sys.argv.pop (0)
		many_algs (sys.argv)
	else: 
		sys.argv.pop (0)
		many_files (sys.argv)


