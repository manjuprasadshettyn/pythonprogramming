# Inheritance

class GeometricObject:
	def __init__(self,color="Green",filled=True):
		self.__color=color
		self.__filled=filled

	def getColor(self):
		return self.__color

	def setColor(self,color):
		self.__color=color

	def isFilled(self):
		return self.__filled

	def setFilled(self,filled):
		self.__filled=filled

	def __str__(self):
		return "Color: " + self.__color + "\nfilled: " + str(self.__filled)