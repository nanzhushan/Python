#!/usr/bin/env python
#coding:utf8
#httplib底层基础模块,实现的功能比较少
"""
"""

import httplib
conn = httplib.HTTPConnection("www.bailingniao.cn",80,False,timeout=100)

##构造请求头部
headers={
    "Host":"www.bailingniao.cn",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Accept":"text/html"
}

conn.request('get','/',headers=headers)

res=conn.getresponse()

##获取头信息
print "获取http协议的版本(11表示http1.1,10表示http1.0): ",res.version
print "返回服务器处理请求的结果说明:",res.reason
print "获取状态:",res.status
print "获取相应的头信息:\n",res.msg
