# Operator Overloading

import math

class Circle:
	def __init__(self,radius):
		self.__radius=radius

	def setRadius(self,radius):
		self.__radius=radius

	def getRadius(self):
		return self.__radius

	def area(self):
		return math.pi * self.__radius ** 2

	def __add__(self,another_circle):
		return Circle(self.__radius + another_circle.__radius) # Circle is used for arithmetic only

	def __gt__(self,another_circle):
		return self.__radius > another_circle.__radius  # no need of Circle for comparision

	def __str__(self):
		return "Circle with radius " + str (self.__radius)

c1=Circle(4)
print("Radius of c1 is:",c1.getRadius())

 
c2=Circle(5)
print("Radius of c2 is:",c2.getRadius())

c3=c1+c2  # overload '+'
print("Radius of c3 is:",c3.getRadius())

if c3 > c2: # overload '>'
	print("Radius of c3 is greater and value is :",c3.getRadius())
else:
	print("Radius of c2 is greater and value is :",c2.getRadius())	

print(c3) # overload 'str'

