# program to find area and perimeter of a circle

from inheritance import GeometricObject

import math

class Circle(GeometricObject):
	def __init__(self,radius):
		GeometricObject.__init__(self)  # we can use super here super().__init__()
		self.__radius=radius

	def getPerimeter(self):
		return 2 * self.__radius * math.pi

	def getArea(self):
		return self.__radius * self.__radius * math.pi
	
	def getRadius(self):
		return self.__radius

	def setRadius(self,radius):
		self.__radius=radius

	def printCircle(self):
		print(self.__str__() + "\nradius: " + str(self.__radius))

	def __str__(self):
		return super().__str__() + "\nradius: " + str(self.__radius)
'''
def main():
	c2 = Circle(10)
	print(c2)
	print("The area of the circle is :",c2.getArea())
	print("The Perimeter of the circle is :",c2.getPerimeter())
	c2.printCircle()
main()
'''
