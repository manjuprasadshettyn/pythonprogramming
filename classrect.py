# program to find area and perimeter of a rectangle

class Rectangle:
	def __init__(self,length=1,width=1):
		self.length=length
		self.width=width

	def getPerimeter(self):
		return 2 * (self.length + self.width)

	def getArea(self):
		return self.length * self.width

	def setSize(self,length,width):
		self.length=length
		self.width=width

def main():
	c1=Rectangle()
	print("The area of the Rectangle of length and width",c1.length,"and",c1.width,"is",c1.getArea())
	print("The Perimeter of the Rectangle of length and width",c1.length,"and",c1.width,"is",c1.getPerimeter())

	c2=Rectangle(5,5)
	print("The area of the Rectangle of length and width",c2.length,"and",c2.width,"is",c2.getArea())
	print("The Perimeter of the Rectangle of length and width",c2.length,"and",c2.width,"is",c2.getPerimeter())

	#Modify radius
	c2.length=2
	c2.width=2
	print("The area of the Rectangle of length and width",c2.length,"and",c2.width,"is",c2.getArea())
	print("The Perimeter of the Rectangle of length and width",c2.length,"and",c2.width,"is",c2.getPerimeter())

	#setSize
	c2.setSize(10,5)
	print("The area of the Rectangle of length and width",c2.length,"and",c2.width,"is",c2.getArea())
	print("The Perimeter of the Rectangle of length and width",c2.length,"and",c2.width,"is",c2.getPerimeter())
main()
