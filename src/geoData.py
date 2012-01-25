class Polygon:
	def __init__(self, geometry):
		self.type = geometry["type"]
		self.polygons = []
		self.getPolygons(geometry["coordinates"])
		self.numberOfPolygons = len(self.polygons)
	def getPolygons(self, geometry):
		if self.type == "Polygon":
			self.polygons.append(geometry[0])
		if self.type == "MultiPolygon":
			for item in geometry:
				self.polygons.append(item)
	
	def printPolygons(self):
		for i in range(len(self.polygons)):
			
			print("Polygon " + str(i) + ": " + str(self.polygons[i]))

class Region:
	def __init__(self, obj):
		properties = obj["properties"]
		geometry = obj["geometry"]
		
		self.name = properties["PLZORT99"]
		self.number = properties["PLZ99"]
		self.geometry = Polygon(geometry)
	
	def getGeometryType(self):
		return type(self.geometry).__name__
	
	def printProperties(self):
		print("Name: " + self.name)
		print("Number: " + self.number)
		print("GeometryType: " + self.getGeometryType())
	
	def printPolygons(self):
		print(self.geometry.type)
		self.geometry.printPolygons()

class GeoData:
	def __init__(self, obj):
		data = obj["features"]
		self.regions = []
		for item in data:
			self.regions.append(Region(item))
	
	def printData(self):
		for item in self.regions:
			item.printProperties()
			item.printPolygons()
			print()
	
	def searchForDuplicatePoint(self, point):
		foundSomething = False
		for region in self.regions:
			for polygon in region.geometry.polygons:
				if polygon.__contains__(point):
					foundSomething = True
					print(region.name + " " + region.number)
		
		if foundSomething == False:
			print("Nothing found!");
	
	def NumberOfPoints(self):
		count = 0
		for region in self.regions:
			for polygon in region.geometry.polygons:
				for point in polygon:
					count = count + 1
		
		return count