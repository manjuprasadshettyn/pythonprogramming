# check if string is a pallindrome

'''str1=input("Enter a string\n")
strr=str1[::-1]
if str1==strr:
	print(str1,"is a pallindrome")
else:
	print(str1,"is not a pallindrome")'''

# Recursive Function

'''def ispallin(s):
	if len(s) <= 1:
		return True
	elif s[0]!=s[len(s)-1]:
		return False
	else:
		return ispallin(s[1:len(s)-1])

str1=input("Enter a string\n")
res=ispallin(str1)
if res:
	print(str1,"is a pallindrome")
else:
	print(str1,"is not a pallindrome")'''


# recursive helper function

def ispallin(s):
	return isPalindromeHelper(s,0,len(s)-1)
def isPalindromeHelper(s,low,high):
	if high <= low:
		return True
	elif s[low]!=s[high]:
		return False
	else:
		return isPalindromeHelper(s,low+1,high-1)

str1=input("Enter a string\n")
res=ispallin(str1)
if res:
	print(str1,"is a pallindrome")
else:
	print(str1,"is not a pallindrome")

