# covert binary to decimal

binary = eval (input("Enter the binary number :"))
print("the Binary  value is:", binary)
i=0
deci=0
while binary !=0 :
 
 digit=binary%10
 binary=binary//10
 deci+=digit*pow(2,i)
 i+=1

print("the decimal value is:", deci)

# another approach

bstring=input("Enter the binary number :")
print("the Binary  value is:", bstring)

decimal=0
exponent=len(bstring)-1

for digit in bstring :
 decimal=decimal+int(digit)*2**exponent
 exponent-=1

print("the decimal value is:", decimal)

