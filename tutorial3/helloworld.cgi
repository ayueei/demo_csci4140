#!/Users/ayueei/miniconda3/bin/python

import cgi

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

if __name__ == '__main__':
	try:
		htmlTop()
		print('hello world')
		htmlTail()
	except:
		cgi.print_exception()