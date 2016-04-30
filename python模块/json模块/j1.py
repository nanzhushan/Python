#coding:utf-8
import json
#print json.__all__
#中括号list

data = [{"name":"qiwsir", "lang":("python", "english"), "age":40}]
print data
print type(data)

data_json = json.dumps(data)
print data_json
print type(data_json)