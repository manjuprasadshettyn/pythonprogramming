# simple calulater

def f(x,y):
	return x+y,x-y,x*y,x/y,x%y

print("Enter two numbers")
x,y=eval(input()) #use , while giving input
#y=eval(input())
print("Simple calculater operations")
t1,t2,t3,t4,t5=f(x,y)
print("Sum:",t1)
print("Difference:",t2)
print("Product:",t3)
print("Quotient:",t4)
print("Remainder:",t5)
