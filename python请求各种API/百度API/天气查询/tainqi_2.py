# -*- coding: utf-8 -*-
#百度的api极力推荐，而且有很多语言的示例 
#http://apistore.baidu.com/

import sys 
import urllib
import urllib2
import json

#url = 'http://apis.baidu.com/apistore/weatherservice/citylist?cityname=%E6%9C%9D%E9%98%B3'
#url = 'http://apis.baidu.com/apistore/weatherservice/citylist?cityname=深圳'
url = 'http://apis.baidu.com/apistore/weatherservice/citylist?cityname=长沙'
req = urllib2.Request(url)

#我的apikey
req.add_header("apikey", "06fa3bb55a60a5b25fef32f3899df496")
resp = urllib2.urlopen(req)
content = resp.read()

#print content

if(content):
    print(content)




