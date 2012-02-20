import tkinter as tk
import tkinter.ttk as ttk

import os
import json

import geoData

class Application:
	def __init__(self):
		pass

	def run(self):
		file = open(os.path.join("input", "data_detailed.json"), "r")
		dataObject = json.loads(file.read())
		file.close()
		data = geoData.GeoData(dataObject)
		#self.data.printData()
		
		#point = [13.873481, 51.12796]
		#self.data.searchForDuplicatePoint(point)
		
		
		#print("Number of points: " + str(self.data.numberOfPoints()))
		#print("unique points:")
		#self.data.searchAllDuplicates()
		
		newData = data.createAggregatedGeoData("041")
		newData.mergePolygons()
		newData.searchAllDuplicates()
		newData.printData()
		#newData.export()
		
		file = open(os.path.join("output", "OUTPUT.json"), "w")
		dataObject = json.dumps(newData.export())
		file.write(dataObject)
		file.close()
		print("File written!")
	
	def createWindow(self):
		root = tk.Tk()
		root.title("GeoMod")
		
		rootFrame = ttk.Frame(root)
		rootFrame.grid(column = 0, row = 0, sticky = (tk.N, tk.S, tk.W, tk.E))
		
		ttk.Label(rootFrame, text="region prefix").grid(column = 0, row = 0)
		
		prefix = tk.StringVar()
		prefix.set("041")
		prefixInput = ttk.Entry(rootFrame, width = 7, textvariable = prefix)
		prefixInput.grid(column = 1, row = 0)
		prefixInput.focus()

		ttk.Button(rootFrame, text = "load area", command = lambda: self.loadArea(prefix.get())).grid(column = 0, row = 1)
		ttk.Button(rootFrame, text = "print all data", command = lambda: self.printData(self.data)).grid(column = 0, row = 2)
		ttk.Button(rootFrame, text = "print aggregated data", command = lambda: self.printData(self.aggregatedData)).grid(column = 0, row = 3)

		option = tk.StringVar(root)
		option.set("convex hull")
		tk.OptionMenu(rootFrame, option, "convex hull", "concave hull").grid(column = 0, row = 4) # TODO make this work with the TTK version
		
		ttk.Button(rootFrame, text = "Draw", command = self.draw).grid(column = 0, row = 5)
		ttk.Button(rootFrame, text = "Work", command = self.run).grid(column = 0, row = 6)
		
		self.canvas = tk.Canvas(rootFrame, width = 400, height = 400, bg = "white")
		self.canvas.grid(column = 2, row = 0, rowspan = 7)
		
		root.mainloop()
	
	def loadArea(self, prefix):
		file = open(os.path.join("input", "data_detailed.json"), "r")
		dataObject = json.loads(file.read())
		file.close()
		self.data = geoData.GeoData(dataObject)
		
		self.aggregatedData = self.data.createAggregatedGeoData(prefix)
		self.aggregatedData.mergePolygons()
		self.aggregatedData.searchAllDuplicates()
	
	def printData(self, data):
		data.printData()
	
	def draw(self):
		self.canvas.create_line(10, 10, 200, 50, fill = "red", width = 10)