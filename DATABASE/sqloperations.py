import MySQLdb

# open a database connection
db=MySQLdb.connect("localhost","root","root","testdb")

# prepare a cursor object using cursor() method
cursor=db.cursor()

# execute SQL query using execute() method
cursor.execute("drop table if exists EMPLOYEE")

# Query to create table
sql="""CREATE TABLE EMPLOYEE(FIRST_NAME CHAR(20) NOT NULL,LAST_NAME CHAR(20),AGE INT,GENDER CHAR(6),INCOME FLOAT)"""
cursor.execute(sql)

# Query to insert into table
try:
	sql1="""insert into EMPLOYEE values("Mac","Mohan",20,"Male",2000.50),("Mrs","Mohan",20,"Female",2000.50)"""
	cursor.execute(sql1)
	db.commit()
except:
	db.rollback()

# Query to update
try:
	sql2="""update EMPLOYEE set age=age+1 where gender='Male'"""
	cursor.execute(sql2)
	db.commit()
except:
	db.rollback()

# Query to delete an entry
try:
	sql4="""delete from EMPLOYEE where gender='Female'"""
	cursor.execute(sql4)
	db.commit()
except:
	db.rollback()
# Query to read values from table
try:
	sql3="""select * from EMPLOYEE"""
	cursor.execute(sql3)
	results=cursor.fetchall()
	for row in results:
		fname=row[0]
		lname=row[1]
		age=row[2]
		gender=row[3]
		income=row[4]
		print "fname=%s,lname=%s,age=%d,gender=%s,income=%f" %(fname,lname,age,gender,income)
except:
	print "Error: Unable to fetch data"



# Disconnect from server
db.close()
