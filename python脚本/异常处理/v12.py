#coding:utf8
import urllib,urllib2
import httplib

url = 'http://112.126.90.68/search/SearchUser.api'
data = {"currentUid":9030088,"term":"13556885667","protocol_ver":1,"type":3,"ver":"2.2"}
post_data = urllib.urlencode(data)

# html = urllib2.urlopen(url,post_data).read()

try:
    html = urllib2.urlopen(url, post_data).read()
    if '9996' in html:
        print "1"
    else:
        print "0"

#有异常执行except
except :
    print "0"
