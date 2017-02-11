from classdemo import Circle

def main():
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
main()
