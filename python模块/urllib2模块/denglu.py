#coding:utf-8
import urllib
import urllib2
import requests
from distutils.log import INFO

url = 'http://127.0.0.1/gongji/login/login.html'
data = {}
data['name'] = 'knight'
data ['password'] = 'knight'

headers = {
           'Accept' :'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Accept-Encoding': 'gzip, deflate',
           'Host':    '127.0.0.1',
           'Cookie':'username=zhoulong',
           'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
           'Referer' : 'http://127.0.0.1/gongji/login/login.html',
           'Connection' : 'Keep-Alive'           
           }

post_data = urllib.urlencode(data)
requ = urllib2.Request(url,post_data,headers)   
try:
    response = urllib2.urlopen(requ)
    status = response.getcode()
    print status
    
except  urllib2.HTTPError, e:
    print e.code
    
#必须对网页进行解码处理
f = response.read().decode("utf-8")
info = response.info()
print info
   