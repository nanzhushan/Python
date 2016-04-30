#coding:utf-8

import urllib
import urllib2
import requests

url = 'http://127.0.0.1/gongji2/login/login1.php'
data = {}
data['name'] = 'knight'
data ['password'] = 'knight'

post_data = urllib.urlencode(data)
requ = urllib2.Request(url,post_data)   

response = urllib2.urlopen(requ)
for i in response:
    print i
