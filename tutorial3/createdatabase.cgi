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
	db = conn.connect(host='localhost', user='root', passwd='')
	cursor = db.cursor()
	return db, cursor

def createDB(db, cursor):
	sql = 'create database exampledb'
	cursor.execute(sql)
	db.commit()

def createEntity(db, cursor):
	sql = 'use exampledb'
	cursor.execute(sql)
	sql = '''create table person
			(personid int not null auto_increment,
			firstname varchar(20) not null,
			lastname varchar(30) not null,
			primary key(personid))'''
	cursor.execute(sql)
	db.commit()


if __name__ == '__main__':
	try:
		htmlTop()
		db, cursor = connectDB()
		createDB(db, cursor)
		createEntity(db, cursor)
		cursor.close()
		htmlTail()
	except:
		cgi.print_exception()