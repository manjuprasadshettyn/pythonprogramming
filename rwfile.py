#write to and read numbers from a file

from random import randint

outfile = open("numbers.txt","w")
for i in range(10) :
 outfile.write(str(randint(0,9))+ " ")

outfile.close()

# add values of numbers in the file

outfile = open("numbers.txt","r")
sum=0

for line in outfile :
 line=line.split()
 for l in line:
  number=int(l)
  sum+=number
 print("The sum is ",sum)
