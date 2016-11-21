#coding:utf8
import urllib,urllib2
import httplib

#定义post地址
url = 'http://112.126.90.68/search/SearchUser.api'
data = {"currentUid":9030088,"term":"13556885667","protocol_ver":1,"type":3,"ver":"2.2"}
post_data = urllib.urlencode(data)

#提交，发送数据，获取返回信息
html = urllib2.urlopen(url,post_data).read()
print html

