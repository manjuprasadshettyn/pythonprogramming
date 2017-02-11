# program to find area and perimeter of a circle

import math

class Circle:
	def __init__(self,radius=1):
		self.radius=radius

	def getPerimeter(self):
		return 2 * self.radius * math.pi

	def getArea(self):
		return self.radius * self.radius * math.pi
	
	def getRadius(self):
		return self.radius

	def setRadius(self,radius):
		self.radius=radius

 # print a table of areas for radius
def printAreas(c,times):
	print("Radius \t\t Area")
	while times >= 1:
		print(c.getRadius(), "\t\t", c.getArea())
		c.radius=c.radius+1
		times-=1

def main():
	myCircle=Circle()
	n=5
	printAreas(myCircle,n)

	# Display myCircle.radius and times

	print("\n Radius is ",myCircle.getRadius())
	print("\n n is ",n)

	
main()
