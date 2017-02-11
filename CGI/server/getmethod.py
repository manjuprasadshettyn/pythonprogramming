#!/usr/bin/env python

#import modules for CGI handling
import cgi, cgitb

#create instance of FieldStorage
form=cgi.FieldStorage()

#Get data from field
first_name=form.getvalue('first_name')
last_name=form.getvalue('last_name')

print "Content-type:text/html\r\n\r\r\n"
print "<html>"
print "<head>"
print "<title>Hello-Third CGI Program</title>"
print "</head>"
print "<body>"
print "<form action='' method='post'>"
print "First Name: <input type='text' name='first_name'> <br/>"
print "Last Name: <input type='text' name='last_name'> <br/>"
print "<input type='submit' value='Submit'/>"
print "</form>"
print "<h2>Hello %s %s </h2>" % (first_name,last_name)
print "</body>"
print "</html>"
