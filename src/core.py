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
		self.canvasWidth = 700
		self.canvasHeight = 700
		
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
		ttk.Button(rootFrame, text = "print all data (slow!)", command = lambda: self.printData(self.data)).grid(column = 0, row = 2)
		ttk.Button(rootFrame, text = "print aggregated data", command = lambda: self.printData(self.aggregatedData)).grid(column = 1, row = 2)

		option = tk.StringVar(root)
		option.set("convex hull")
		tk.OptionMenu(rootFrame, option, "convex hull", "concave hull").grid(column = 0, row = 4) # TODO make this work with the TTK version
		
		ttk.Button(rootFrame, text = "draw merged area", command = lambda: self.drawArea(self.aggregatedData, "black", "", 2, False)).grid(column = 0, row = 5)
		#ttk.Button(rootFrame, text = "Work", command = self.run).grid(column = 0, row = 6)
		
		self.canvas = tk.Canvas(rootFrame, width = self.canvasWidth, height = self.canvasHeight, bg = "white")
		self.canvas.grid(column = 2, row = 0, rowspan = 7)
		
		#points = [150, 100, 200, 120, 240, 180, 210, 200, 150, 150, 100, 200]
		#p = self.canvas.create_polygon(points, outline = "red", fill = "green", width = 2)
		#self.canvas.scale(p, 100, 100, 2, 2)
		
		root.mainloop()
	
	def loadArea(self, prefix):
		file = open(os.path.join("input", "data_detailed.json"), "r")
		dataObject = json.loads(file.read())
		file.close()
		self.data = geoData.GeoData(dataObject)
		
		self.aggregatedData = self.data.createAggregatedGeoData(prefix)
		self.drawArea(self.aggregatedData, "green", "red", 5)
		
		self.aggregatedData.mergePolygons()
		self.aggregatedData.searchAllDuplicates()
	
	def printData(self, data):
		data.printData()
	
	def drawArea(self, data, outerColor = "black", innerColor = "white", strokeWidth = 5, delete = True):
		xMin = 180
		xMax = -180
		yMin = 90
		yMax = -90
		
		#get minimum and maximum values first so scaling everything later will not be necessary
		for region in data.regions:
			for polygon in region.geometry.polygons:
				for point in polygon:
					if point[0] < xMin:
						xMin = point[0]
					if point[0] > xMax:
						xMax = point[0]
					if point[1] < yMin:
						yMin = point[1]
					if point[1] > yMax:
						yMax = point[1]
		
		print("xMin: " + str(xMin))
		print("xMax: " + str(xMax))
		print("yMin: " + str(yMin))
		print("yMax: " + str(yMax))
		
		#draw
		if(delete == True):
			self.canvas.delete(tk.ALL)

		for region in data.regions:
			for polygon in region.geometry.polygons:
				points = []
				for point in polygon:
					points.append(((point[0] - xMin) / (xMax - xMin)) * self.canvasWidth)
					points.append(((point[1] - yMin) / (yMax - yMin)) * self.canvasHeight)
				p = self.canvas.create_polygon(points, outline = outerColor, fill = innerColor, width = strokeWidth)