# swap using simultaneous assignment more than 2 numbers

a = eval (input(" Enter the first number "))
b = eval (input(" Enter the second number "))
c = eval (input(" Enter the second number "))
d = eval (input(" Enter the second number "))
e = eval (input(" Enter the second number "))

print ("Before swapping X and Y is" , a ,b, c, d, e )

a,b,c,d,e=e,d,c,b,a

print ("After swapping X and Y is" , a ,b, c, d, e)




