# polymorphism

from inheritancetest import Circle
from inheritancerect import Rectangle

import math

def main():
	# display circle and rectangle properties

	c=Circle(1)
	r=Rectangle(1,math.pi)

	displayObject(c)
	displayObject(r)

	print("Are the Circle and Rectangle of the same size ?", issameArea(c,r))

def displayObject(g):
	print(g.__str__())

def issameArea(g1,g2):
	return g1.getArea() == g2.getArea()

main()
