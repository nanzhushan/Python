#coding:utf-8
#示例   http://127.0.0.1/gongji/login/login.html
import urllib
import urllib2

aa = {'user':'knight','pasword':'knight'}
cc = urllib.urlencode(aa)
#print "this is %s" %(cc)

url = 'http://127.0.0.1/gongji/login/login.html' 
#print url 
print urllib2.urlopen(url,cc).read()
 