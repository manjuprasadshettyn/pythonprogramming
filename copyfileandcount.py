import os.path

fname=input("Enter the name of the file \n")
count=0
if os.path.exists(fname) :
 print("File name already exists")
 infile = open(fname,"r")
 data=infile.read()
 for x in data :
  if x=='\n' :
   count+=1
 print("the number of lines is ",count)
 print("the number of characters read is", len(data)-count)
 
 outfile = open("sampleout","w")
 outfile.write(data)
 outfile.close()
 infile.close()

else :
 print("File name doesnot exixt") 
  

