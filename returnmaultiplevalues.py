# returning multiple values

'''def sort(num1,num2):
	if num1 < num2:
		return num1,num2
	else:
		return num2,num1

n1,n2=sort(3,2)
print("n1 is ",n1)
print("n2 is ",n2) '''

def f(x,y):
	return x+y,x-y,x*y,x/y

t1,t2,t3,t4=f(9,5)
print("Sum:",t1)
print("Difference:",t2)
print("Product:",t3)
print("Quotient:",t4)
