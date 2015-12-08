class Vector2D(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __add__(self, other):
		sumvector = Vector2D(self.x+other.x, self.y+other.y)
		return sumvector
	def __mul__(self, other):
		mulvec = Vector2D(self.x*other, self.y*other)
		return mulvec
	def __neg__(self):
		negvec=Vector2D(self.x*(-1), self.y*(-1))
		return negvec
	def __abs__(self):
		absvec = math.sqrt(self.x**2+self.y**2)
		return absvec
	def __repr__(self):
		return "Vector2D(%s, %s)"%(self.x, self.y)
