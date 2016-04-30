#!/usr/bin/python
#coding:utf-8
#带有html表单的python cgi的问候脚本
import cgi
form = cgi.FieldStorage()

#此处可以用三个单引号也可以用三个双引号

print """Content-type: text/html;charset=utf-8\n\n

<html>
<head>Greeting Page</head>
<body>

<h1>Hello,world</h1>


<form action='c1.py'>
Change name<input type='text' name='name'>
<input type='submit'>
</form>


</body>

</html>

"""
