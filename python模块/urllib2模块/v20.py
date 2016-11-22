#coding:utf8
import urllib,urllib2
import httplib
import requests
import json


url = 'http://112.126.90.68/search/SearchUser.api'
data = {"currentUid":9030088,"term":"13556885667","protocol_ver":1,"type":3,"ver":"2.2"}
post_data = urllib.urlencode(data)

r = requests.post(url,data=post_data)

print r.json()
print r.json().get('errcode')
