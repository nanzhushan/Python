#coding:utf-8
#参看地址;https://github.com/qiwsir/StarterLearningPython/blob/master/227.md
#api address:http://apistore.baidu.com/astore/serviceinfo/1798.html
#说明:只能查询当天的天气
import sys 
import urllib
import urllib2
import json
#url = 'http://apistore.baidu.com/microservice/weather?citypinyin=shenzhen'
url = 'http://apistore.baidu.com/microservice/weather?citypinyin='
city = raw_input("输入你想查询城市的名称拼音:")  
#rint city
url_all = url + city    #完整的URL
#rint url_all
req = urllib2.Request(url_all)
resp = urllib2.urlopen(req)
content = resp.read()
#print type(content)      #是字符串类型
#用load方法转换
new_content = json.loads(content)   
 
#print type(new_content)
#print new_content
cc = new_content['retData']   ###ok
#print type(cc)
#print cc
print "城市:",cc['city']
print "发布时间 ",cc['date'],cc['time']
print "邮编:",cc['postCode']
print "海拔:",cc['altitude'],"米"
print "天气情况：",cc['weather']
print "气温：",cc['temp']
print "最低气温：",cc['l_tmp']
print "最高气温：",cc['h_tmp']
print "风向：",cc['WD']
print "风力：",cc['WS']
print "日出时间:",cc['sunrise']
print "日落时间:",cc['sunset']

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


