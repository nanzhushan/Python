#coding:utf8
import urllib,urllib2
import httplib
import json

url = 'http://112.126.90.68/search/SearchUser.api'
data = {"currentUid":9030088,"term":"13556885667","protocol_ver":1,"type":3,"ver":"2.2"}
dd = json.dumps(data)


try:
    html = urllib2.urlopen(url, dd).read()
    ff = html[20:23]
    if ff == '200':
        print "1"
    else:
        print "0"
except:
    print 0
