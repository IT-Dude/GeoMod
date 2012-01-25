class Region:
	def __init__(self, obj):
		self.geometry = obj["geometry"]
		self.type = obj["type"]
		self.properties = obj["properties"]
		print(self.properties)
		pass


class GeoData:
	def __init__(self, obj):
		self.type = obj["type"]
		self.features = obj["features"]
		self.regions = []
		for item in self.features:
			self.regions.append(Region(item))
	
	def printData(self):
		#print(self.features)
		pass