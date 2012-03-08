class Point:
	def __init__(self, newX, newY):
		self.x = newX
		self.y = newY

#                  N3
#	  Vert1 X+++++++++++++++X Vert2
#			 +             +
#			  +           +
#			   +         +
#			N2  +       +  N1
#			     +     +
#			      +   +
#				   + +
#					X
#                 Vert3

class Triangle:
	def __init__(self):
		self.vertices = []
		self.neighborTriangles = []

class Polygon:
	def __init__(self):
		self.vertices = []
	
	def split(self):
		pass
	
	def join(self):
		pass