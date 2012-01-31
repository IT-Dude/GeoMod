#import tkinter as tk
#import tkinter.ttk as ttk

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
		self.data = geoData.GeoData(dataObject)
		#self.data.printData()
		
		#point = [13.873481, 51.12796]
		#self.data.searchForDuplicatePoint(point)
		
		
		#print("Number of points: " + str(self.data.numberOfPoints()))
		#print("unique points:")
		#self.data.searchAllDuplicates()
		
		newData = self.data.createAggregatedGeoData("041")
		newData.mergePolygons()
		newData.searchAllDuplicates()
		newData.printData()
		#newData.export()
		
		file = open(os.path.join("output", "OUTPUT.json"), "w")
		dataObject = json.dumps(newData.export())
		file.write(dataObject)
		file.close()
		print("File written!")