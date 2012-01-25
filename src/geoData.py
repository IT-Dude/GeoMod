class Polygon:
	def __init__(self, geometry):
		self.coordinates = geometry[0]
		pass

class PolygonMulti:
	def __init__(self, geometry):
		pass

class Region:
	def __init__(self, obj):
		properties = obj["properties"]
		geometry = obj["geometry"]
		
		self.name = properties["PLZORT99"]
		self.number = properties["PLZ99"]
		self.geometry = self.getGeometry(geometry)
	
	def getGeometry(self, geometry):
		if geometry["type"] == "Polygon":
			return Polygon(geometry["coordinates"])
		else:
			return PolygonMulti(geometry["coordinates"])
	
	def getGeometryType(self):
		return type(self.geometry).__name__
	
	def printData(self):
		print("Name: " + self.name)
		print("Number: " + self.name)
		print("GeometryType: " + self.getGeometryType())

class GeoData:
	def __init__(self, obj):
		data = obj["features"]
		self.regions = []
		for item in data:
			self.regions.append(Region(item))
	
	def printData(self):
		for item in self.regions:
			item.printData()
		pass