#coding:utf8
import json
url_list = ["http://baidu.com","http://www.qq.com","http://www.sina.com.cn"]
web_list=[]
web_dict={"data":None}

for url in url_list:
    url_dict = {}
    url_dict["{#SITENAME}"] = url
    web_list.append(url_dict)
    web_dict["data"] = web_list

print web_dict
print type(web_dict)

#dict转str,成为json格式数据
jsonStr = json.dumps(web_dict,sort_keys=True,indent=4)
print jsonStr
print type(jsonStr)

