# Tail recursive factorial program

def fact(x):
	return facthelper(x,1)
def facthelper(n,result):
	if n==0:
		return result
	elif n==1:
		return result
	else:
		return facthelper(n-1,n*result)

print("Enter the number to find the factorial")
num=int(input())

print("The factorial of ",num,"is",fact(num))
