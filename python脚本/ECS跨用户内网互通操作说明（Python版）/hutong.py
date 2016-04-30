#coding=utf-8
import sys
import urllib,urllib2
import base64
import hmac  ##加密
from hashlib import sha1
import time
import uuid


print "请输入相关信息，注意不要有空格"

a_id_1 = raw_input("请输入用户1的ID:\n")
a_key_1 = raw_input("请输入用户1的key\n")

'''
#输出进行测试
print a_id_1
'''
jifang = raw_input("请输入您的机房的汉语拼音（小写）:\n")  #值为All或者List如果是List,下面两个账号下的List需要写好#
jifang_name='cn-' + jifang
##测试输出
#print jifang_name 

mode=raw_input("请输入模式如果是账号下全环境请输入ALL,如果是机器批量输入List:\n")

if mode == "List":
    print "输入格式为（'i-e1','i-e2'）"
    
    

if mode == "ALL":
    print "输入格式为all"
  
           
    
    
    
    
    
    
