try:
	n=eval(input("Enter a number: "))
	print("The number entered is",n)
except NameError as ex:
	print("Exception:",ex)
