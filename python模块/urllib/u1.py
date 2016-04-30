#coding:utf-8
#像curl等内容，需要用read()方法打开
#urlopen()建立了文件对象，需要用read方法进行读

import urllib
a = urllib.urlopen("http://www.winbons.com/")
#print a.read()
#返回头信息
print a.info()
#返回http状态码
print a.getcode()
#返回url
print a.geturl()







