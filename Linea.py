import os

import sublime, sublime_plugin

import functools

import subprocess
 
class lineaCommand(sublime_plugin.WindowCommand):
    def run(self, dirs):
    	self.window.show_input_panel("Widget name:", "", functools.partial(self.on_done, dirs[0]), None, None)

    def on_done(self, dir, name):
		p = subprocess.Popen('linea generate widget "' + dir + "\\" + name + '"', stdout=subprocess.PIPE, shell=True)
		(output, err) = p.communicate()
		print output

    def is_enabled(self, dirs):
        return len(dirs) > 0