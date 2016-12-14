#coding:utf8
import os,sys,json
url_list = ["http://baidu.com","http://www.qq.com","http://www.sina.com.cn"]

def web_site_discovery():
    web_list=[]
    web_dict={"data":None}

    for url in url_list:
        url_dict={}
        url_dict["{#SITENAME}"] = url
        web_list.append(url_dict)

    web_dict["data"]=web_list
    jsonStr = json.dumps(web_dict,sort_keys=True,indent=4)
    return jsonStr

print web_site_discovery()