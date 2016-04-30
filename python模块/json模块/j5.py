#coding:utf-8
#Python可以使用解码JSON demjson.decode()函数。这个函数返回值从json解码适当的Python类型
import demjson
import json

json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
cc = 'aa,fda .cc'
#print type(cc)
#print len(cc)    #把标点符号和空格都算进去

print type(json)
#print len(json)   ##字符串长度,也就是字符串元素个数

text = demjson.decode(json)  #解码成python对象
print type(text)       #字典类型
#print len(text)      #长度
print text['b']

