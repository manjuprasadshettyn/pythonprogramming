# reading from csvfile

import csv

with open("name.csv") as csvfile:
	readcsv=csv.reader(csvfile,delimiter=' ')
	for row in readcsv:
		print(row)
		print(row[0],row[1],row[2])



'''
# approach 2

import csv

csvfile=open("name.csv")
r=csv.reader(csvfile,delimiter=' ')
for row in r:
	print(row[0],row[1],row[2])
'''
	
