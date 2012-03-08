class Point:
	def __init__(self, newX, newY):
		self.x = newX
		self.y = newY

class Triangle:
	def __init__(self):
		self.vertices = []
		self.neighborTriangles = []