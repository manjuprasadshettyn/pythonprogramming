# recursive binary search

def binsearch(s,k):
	return binsearchHelper(s,k,0,len(s)-1)
def binsearchHelper(s,k,low,high):
	if low > high:
		return -1
	mid=(low+high)//2
	if s[mid]==k:
		return mid+1

	elif s[mid] < k:
		return binsearchHelper(s,k,mid+1,high)
	else:
		return binsearchHelper(s,k,low,mid-1)

arr=[int(x) for x in input("enter the numbers\n").split()]
key=int(input("Enter the key to be searched\n"))
arr.sort()
print("entered elements in sorted order is",arr)
pos=binsearch(arr,key)
print(pos)
if pos!=-1:
	print(key,"found at position",pos)
else:
	print(key,"not found")
