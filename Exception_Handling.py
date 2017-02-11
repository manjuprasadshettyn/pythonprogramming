# Exception

try:
	num1,num2=eval(input("Enter two numbers separated by a comma "))
	result=num1/num2
	print("Result is",result)

except ZeroDivisionError:
	print("Division by Zero")

except SyntaxError:
	print("A comma may be missing in the input")

except:
	print("Something is wrong in input")

else:
	print("No exceptions")

finally:
	print("The finally clause is executed")
