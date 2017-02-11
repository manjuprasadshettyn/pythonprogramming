# program to find area and perimeter of a rectangle

from inheritance import GeometricObject

class Rectangle(GeometricObject):
	def __init__(self,length=1,width=1):
		GeometricObject.__init__(self)
		self.__length=length
		self.__width=width

	def getPerimeter(self):
		return 2 * (self.__length + self.__width)

	def getArea(self):
		return self.__length * self.__width

	def setSize(self,length,width):
		self.__length=length
		self.__width=width
	def printRect(self):
		print(self.__str__() + "\nLength: " + str(self.__length) + "\nWidth: " + str(self.__width))

	def __str__(self):
		return super().__str__() + "\nLength: " + str(self.__length) + "\nWidth: " + str(self.__width)

'''def main():
	c2=Rectangle(5,5)
	print(c2)
	print("The area of the Rectangle is:", c2.getArea())
	print("The Perimeter of the Rectangle is :", c2.getPerimeter())
	c2.printRect()
main()
'''
