# Nested loops
print("       MULTIPLICATION TABLE       \n") 
print(end='      ')
for i in range(1,11) :
 print(" ",i,end='  ')

print() #jump to the new line
print("________________________________________________________")

# display the table body

for i in range(1,10) :
 print(i," |",end=' ')
 for j in range(1,11):
  print(format(i*j , "4d"),end=' ')
 print()

print(10,"|",end=' ')
for j in range(1,11):
  print(format(10*j , "4d"),end=' ')

print()
