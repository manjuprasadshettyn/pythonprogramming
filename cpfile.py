
infile=open("Sample.txt","r")
print("Copying file")
value=infile.read()
outfile = open("Filecopy.txt","w")
outfile.write(value)
outfile.close()
infile.close()
