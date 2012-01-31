class Polygon:
	def __init__(self, geometry):
		if geometry != None: # TODO holy cow! are you insane???
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
		if obj != None: # TODO ffs, fix this! ASAP!!!
			properties = obj["properties"]
			geometry = obj["geometry"]
			
			self.name = properties["PLZORT99"]
			self.number = properties["PLZ99"]
			self.geometry = Polygon(geometry)
	
	def getGeometryType(self):
		return type(self.geometry).__name__
	
	def printProperties(self):
		print("Name: " + self.name)
		print("Number: " + str(self.number))
		print("GeometryType: " + self.getGeometryType())
	
	def printPolygons(self):
		print(self.geometry.type)
		self.geometry.printPolygons()

class GeoData:
	def __init__(self, obj, regions=None): # TODO dude, write better code!!!
		if obj != None:
			data = obj["features"]
			self.regions = []
			for item in data:
				self.regions.append(Region(item))
			print("Loading finished!")
		
		if regions!= None:
			self.regions = regions
	
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
	
	def numberOfPoints(self):
		count = 0
		for region in self.regions:
			for polygon in region.geometry.polygons:
				for point in polygon:
					count = count + 1
		return count

	def createAggregatedGeoData(self, prefix):
		aggregatedRegions = []
		for region in self.regions:
			if region.number.startswith(prefix):
				aggregatedRegions.append(region)
		return GeoData(None, aggregatedRegions)

	def mergePolygons(self):
		polygons = []
		for region in self.regions:
			for polygon in region.geometry.polygons:
				polygons.append(polygon)
		
		edges = set()
		for polygon in polygons:
			for i in range(len(polygon)):
				if i < (len(polygon) - 1):
					edge = Edge(polygon[i], polygon[i + 1])
				else:
					edge = Edge(polygon[i], polygon[0])
				edges.add(edge)
		
		mergedPolygon = []
		edgeList = list(edges)
		
		selectedEdge = edgeList[0]
		selectedPoint = selectedEdge.start
		
		mergedPolygon.append(selectedPoint)
		
		while len(edgeList) != 0:
			foundEdge = None
			for edge in edgeList:
				if edge.contains(selectedPoint):
					if edge != selectedEdge:
						foundEdge = edge
						
			
			
		
		print(mergedPolygon)
		

class Edge:
	def __init__(self, start, end):
		self.start = start
		self.end = end
	
	def contains(self, value):
		if value == self.start:
			return True
		elif value == self.end:
			return True
		else:
			return False