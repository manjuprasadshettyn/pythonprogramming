# factorial of a function using recursion

def fact(x):
	if x==0:
		return 1
	elif x==1:
		return 1
	else:
		return x*fact(x-1)

print("Enter the number to find the factorial")
num=int(input())

print("The factorial of ",num,"is",fact(num))
