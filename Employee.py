class Employee:
	def __init__(self,name=" ",design=" ",salary="10000",DA=0.8,HRA=0.1):
		self.__name=name
		self.__design=design
		self.__salary=salary
		self.__DA=DA
		self.__HRA=HRA

	def getName(self):
		return self.__name

	def getDesign(self):
		return self.__design

	def getSalary(self):
		return self.__salary
	
	def getDA(self):
		return self.__DA

	def getHRA(self):
		return self.__HRA

	def setName(self):
		self.__name=name

	def setDesign(self):
		self.__design=design

	def setSalary(self):
		self.__salary=salary
	
	def setDA(self):
		self.__DA=DA

	def setHRA(self):
		self.__HRA=HRA

	def grosssalary(self):
		gross=self.__salary+(self.__salary * self.__DA)+(self.__salary * self.__HRA)
		return gross
		
