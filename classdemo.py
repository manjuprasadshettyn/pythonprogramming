# program to find area and perimeter of a circle

import math

class Circle:
	def __init__(self,radius=1):
		self.radius=radius

	def getPerimeter(self):
		return 2 * self.radius * math.pi

	def getArea(self):
		return self.radius * self.radius * math.pi

	def setRadius(self,radius):
		self.radius=radius

'''def main():
	c1=Circle()
	print("The area of the circle of radius",c1.radius,"is",c1.getArea())
	print("The Perimeter of the circle of radius",c1.radius,"is",c1.getPerimeter())
	c2=Circle(5)
	print("The area of the circle of radius",c2.radius,"is",c2.getArea())
	print("The Perimeter of the circle of radius",c2.radius,"is",c2.getPerimeter())
	#Modify radius
	c2.radius=15
	print("The area of the circle of radius",c2.radius,"is",c2.getArea())
	print("The Perimeter of the circle of radius",c2.radius,"is",c2.getPerimeter())
main()'''
