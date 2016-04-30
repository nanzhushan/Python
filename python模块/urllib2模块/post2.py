#coding:utf-8
import urllib
import urllib2
aa = {'name':'knight','pasword':'knight'}

request = urllib2.Request('http://127.0.0.1/gongji/login/login.html')
print 'this is:' ,request.get_method()

request.add_data(urllib.urlencode(aa))
print 'this is 2:',request.get_method()

request.add_header('333', '4444')
print request.get_data()
print '...........'
print urllib2.urlopen(request).read()