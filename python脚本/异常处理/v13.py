#coding:utf8
import urllib,urllib2
import httplib

url = 'http://112.126.90.68/search/SearchUser.api'
data = {"currentUid":9030088,"term":"13556885667","protocol_ver":1,"type":3,"ver":"2.2"}
post_data = urllib.urlencode(data)
try:
    html = urllib2.urlopen(url, post_data).read()
    if '9996' in html:
        print "1"
    else:
        print "0"

#except 后面接错误类型表示要匹配的错误类型
#except  如果没有接错误类型就是匹配所有
except :
    pass    #忽略异常
    print "0"
