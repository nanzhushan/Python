#coding:utf-8
import json
#print json.__all__
#中括号list

data = [{"name":"qiwsir", "lang":("python", "english"), "age":40}]
#print data
#print type(data)

data_json = json.dumps(data)
#print data_json
#print type(data_json)
#展现好阅读
#sort_keys=True意思是按照键的字典顺序排序，indent=2是让每个键值对显示的时候，以缩进两个字符对齐
data_j = json.dumps(data,sort_keys=True,indent=2)
print data_j
