#The following program computes and displays the area of a rectangle. The
#area of a rectangle is the multiplication of length and width, and their
#values will be supplied by the user. The values supplied by the user will be
#through the input() function, which returns the supplied values in string
#format and hence will be converted into the integer data type using the
#int() function.

l=input("Enter length: ")
b=input("Enter width: ")
a=int(l)*int(b)
print ("Area of rectangle is",a)
