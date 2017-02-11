'''# example for __eq__()

class A:
	def __init__(self,i):
		self.i=i

	def __str__(self):
		return "A"

	def __eq__(self,other):
		return self.i == other.i

x=A(6)
y=A(7)

print(x==y)


# exaample for __str__()

class A:
	def __init__(self,i):
		self.i=i


	def m1(self):
		self.i+=1

	def __str__(self):
		return str(self.i)

x=A(8)
print(x)

'''

#
class A:
	def __init__(self,i=0):
		self.i=i

	def m1(self):
		self.i+=1

class B(A):
	def __init__(self,j=0):
		super().__init__(3)
		self.j=j

	def m1(self):
		self.i+=1

b=B()
b.m1()
print(b.i)
print(b.j)

