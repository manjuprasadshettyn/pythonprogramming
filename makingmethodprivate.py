# private Methods

class P:
	def __init__(self,name,alias):
		self.name=name
		self.__alias=alias
	
	def who(self):
		print("Name:",self.name)
		print("Alias:",self.__alias)

	def __foo(self):
		print("This is private method")

	def foo(self):
		print("This is public method")
		self.__foo() #call the private method


def main():
	obj=P("Manjuprasad","MP")
	obj.who()
	obj.foo()     # call for public method
	#obj.__foo()  # can't access because its a private member
	obj._P__foo() # call for private method

main()


