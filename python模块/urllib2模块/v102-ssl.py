#coding:utf8
import urllib,urllib2
import httplib
import json
import ssl

#官方文档: https://www.python.org/dev/peps/pep-0476/

context = ssl._create_unverified_context()

url="https://iosprod.quncaotech.com/homepage/nearbyPlayerList.api"

data = {"ver":"1.0","protocol_ver":1,"lng":110.16545,"lat":22.464,"cityId":6,"pageNum":0,"pageSize":50}
post_data = json.dumps(data)

html = urllib2.urlopen(url,post_data,context=context).read()
print html
print type(html)


