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

def createPersonList():
	people = []
	people.append(["yue", "wang"])
	people.append(["abc", "efg"])
	people.append(["hijk", "lmn"])
	people.append(["opu", "rst"])
	people.append(["uvw", "xyz"])
	return people

def insertPeople(db, cursor, people):
	for each in people:
		sql = "insert into person(firstname, lastname) values('%s','%s')" % (each[0], each[1])
		cursor.execute(sql)
	db.commit()


if __name__ == '__main__':
	try:
		htmlTop()
		db, cursor = connectDB()
		people = createPersonList()
		insertPeople(db, cursor, people)
		cursor.close()
		htmlTail()
	except:
		cgi.print_exception()