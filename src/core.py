import tkinter as tk
import tkinter.ttk as ttk

class Application:
	def __init__(self):
		print("foo")
		self.root = tk.Tk()
		ttk.Button(self.root, text="Work!").grid()
	
	def run(self):
		self.root.mainloop()