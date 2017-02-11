# Custom exception

import math

class Circle:
	def __init__(self,radius):
		self.__radius=radius

	def setRadius(self,radius):
		if radius < 0:
			raise InvalidradiusException(radius)
		else:
			self.__radius=radius

	def getRadius(self):
		return self.__radius

	def area(self):
		return math.pi * self.__radius ** 2

class InvalidradiusException(RuntimeError):
	def __init__(self,radius):
		super().__init__()
		self.radius=radius


try:
	c1=Circle(4)
	print("Radius of c1 is:",c1.area())

 
	c2=Circle(5)
	print("Radius of c2 is:",c2.area())

	c3=Circle(-1)
	c3.setRadius(-1)
	print("Radius of c3 is:",c3.area())	
except InvalidradiusException as ex:
	print("The radius", ex.radius,"is invalid")

except Exception:
	print("something is wrong")
