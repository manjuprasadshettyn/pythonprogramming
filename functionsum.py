# function to find the sum of series

def sum1(a,b):
	sum=0
	for i in range(a,b+1) :
		sum+=i
	return sum

print("the sum of integers from 1 to 10 is ", sum1(1,10))
print("the sum of integers from 20 to 37 is ", sum1(20,37))
print("the sum of integers from 35 to 49 is ", sum1(35,49))

