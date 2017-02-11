# decimal to binary conversion

decimal = eval (input("Enter the decimal number :"))
print("the Decimal value is:", decimal)
i=0
binary=0
while decimal !=0 :
 
 digit=decimal%2
 decimal=decimal//2
 binary+=digit*pow(10,i)
 i+=1

print("the binary value is:", binary)



# another approach

decimal=int(input("Enter a decimal integer:"))
if decimal == 0 :
 print(0)
else:
 print("Quotient Remainder Binary")
 bstring=" "
 while decimal > 0 :
  remainder=decimal % 2
  decimal=decimal // 2
  bstring=str(remainder) + bstring
  print("%5d%8d%12s" % (decimal,remainder,bstring))
 print("The binary representation is ", bstring)
