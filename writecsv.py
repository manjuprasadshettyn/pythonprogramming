# write content to a csv file
'''
import csv

data=["First_Name,Last_Name,City".split(","),"John,Dsouza,Mangalore".split(","),"Ram,Rao,Udupi".split(",")]

with open('name1.csv','w') as csv_file:
	writer=csv.writer(csv_file,delimiter=',')
	for line in data:
		writer.writerow(line)
csv_file.close()

'''
#approah 2


import csv

data=["First_Name,Last_Name,City".split(","),"John,Dsouza,Mangalore".split(","),"Ram,Rao,Udupi".split(",")]

csv_file=open('name1.csv','w')
writer=csv.writer(csv_file,delimiter=',')
for line in data:
	writer.writerow(line)
csv_file.close()


