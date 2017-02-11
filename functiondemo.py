# demo function to find the largest of 2  numbers

def largest(a,b):
	if a > b:
		print(a," is largest")
	elif a < b:
		print(b," is largest")
	else:
		print("both are equal")


def main():
	x,y=10,20
	largest(x,y)

main()
