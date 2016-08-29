urllib:

GET方式

f=urllib.urlopen("http://m.cnblogs.com/")
s=f.read()
print s
带参数

params = urllib.urlencode({'id': 8, 'name': 'jack', 'age': 25})
f = urllib.urlopen("http://localhost:18797/MailClient/test.aspx?%s" % params)
print f.read()