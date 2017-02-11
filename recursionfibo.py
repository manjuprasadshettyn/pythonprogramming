# fibonacci series using recursion

def fibo(n):

	if n==0:
		return 0
	if n==1:
		return 1
	else:
		return fibo(n-1)+fibo(n-2)

print("enter a number")
num=int(input())
print("Fibonacci series is")
for i in range(0,num):
	print(fibo(i),end=" ")
print()
