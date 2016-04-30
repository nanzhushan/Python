#coding:utf-8
'''
采用get方法，对参数编码并追加到url
'''

import urllib
cc = {'a':'string','foo':'bar'}
dd = urllib.urlencode(cc)
print 'enconde:...', dd
url = 'http://127.0.0.1/1.html/?' + dd
print url
#print urllib.urlopen(url).read()
