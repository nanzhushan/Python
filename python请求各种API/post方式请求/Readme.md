POST方式：

params = urllib.urlencode({'id': 8, 'name': 'jack', 'age': 25})
f = urllib.urlopen("http://localhost:18797/MailClient/test.aspx",params)
print f.read()
函数原型

urllib.urlopen(url[, data[, proxies]]) 
urllib2
可以详细的定义header参数

httplib
最底层更灵活更强大的http请求和响应