#!/usr/bin/python
from __future__ import print_function
import cgi
import mysql.connector as conn

def htmlTop():
	print("""Content-type:text/html\n\n
			 <!DOCTYPE html>
			 <html lang='en'>
			 	<head>
			 		<meta charset='utf-8'/>
			 		<title>My server-side template</title>
		 		</head>
		 		<body>""")

def htmlTail():
	print("""</body>
			</html>""")

def connectDB():
	db = conn.connect(host='localhost', user='root', passwd='', db='exampledb')
	cursor = db.cursor()
	return db, cursor

def selectPeople(db, cursor):
	sql = "select * from person"
	cursor.execute(sql)
	people = cursor.fetchall()
	return people

def displayPeople(people):
	print("<table border='1'>")
	print("<tr>")
	print("<th>ID</th>")
	print("<th>First Name</th>")
	print("<th>Last Name</th>")
	print("</tr>")
	for each in people:
		print("<tr>")
		print("<td>%s</td>" % each[0])
		print("<td>%s</td>" % each[1])
		print("<td>%s</td>" % each[2])
		print("</tr>")
	print("</table>")




if __name__ == '__main__':
	try:
		htmlTop()
		db, cursor = connectDB()
		people = selectPeople(db, cursor)
		cursor.close()
		displayPeople(people)
		htmlTail()
	except:
		cgi.print_exception()