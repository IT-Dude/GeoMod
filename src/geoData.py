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
		print("Loading finished!")
	
	def printData(self):
		for item in self.regions:
			item.printProperties()
			item.printPolygons()
			print()
	
	def searchForDuplicatePoint(self, point):
		count = 0
		for region in self.regions:
			for polygon in region.geometry.polygons:
				if polygon.__contains__(point):
					count = count + 1
					print(region.name + " " + region.number)
		
		if count <= 1:
			print("Nothing found!");
	
	def searchAllDuplicates(self):
		pointDuplicates = []
		pointNonDuplicates = []
		
		for region in self.regions:
			for polygon in region.geometry.polygons:
				for point in polygon:
					pointNonDuplicates.append(point)
					
					for region2 in self.regions:
						for polygon2 in region2.geometry.polygons:
							if polygon != polygon2:
								if polygon2.__contains__(point):
									pointDuplicates.append(point)
									if pointNonDuplicates.__contains__(point):
										pointNonDuplicates.remove(point)
		
		print(pointNonDuplicates)
	
	def NumberOfPoints(self):
		count = 0
		for region in self.regions:
			for polygon in region.geometry.polygons:
				for point in polygon:
					count = count + 1
		
		return count

	def aggregatePolygons(self, prefix):
		aggregatedRegions = []
		for region in self.regions:
			if region.number.startswith(prefix):
				aggregatedRegions.append(region)