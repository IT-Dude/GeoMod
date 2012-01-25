#import tkinter as tk
#import tkinter.ttk as ttk
import os

class Application:
	def __init__(self):
		pass

	def run(self):
		file = open(os.path.join("input", "data_test.json"), "r")
		data = file.read()
		file.close()
		print(data)