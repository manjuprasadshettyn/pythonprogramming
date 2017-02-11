# reading from a file

infile=open("Sample.txt","r")
print("(1) using read() :")
print(infile.read())
infile.close()

infile=open("Sample.txt","r")
print("(2) using read(number) :")
s1=infile.read(4)
print(s1)
s2=infile.read(10)
print(repr(s2))
infile.close()

infile=open("Sample.txt","r")
print("(3) using readline() :")
line1=infile.readline()
line2=infile.readline()
line3=infile.readline()
print(repr(line1))
print(repr(line2))
print(repr(line3))
infile.close()

infile=open("Sample.txt","r")
print("(4) using readlines() :")
print(infile.readlines())
infile.close()

# reading all data from a file

infile=open("Sample.txt","r")
for line in infile :
 print(line)
infile.close()

