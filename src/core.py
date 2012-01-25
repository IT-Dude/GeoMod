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
		
		#point = [ 13.294614, 51.316341 ]
		#self.data.searchForDuplicatePoint(point)
		
		print(self.data.NumberOfPoints())