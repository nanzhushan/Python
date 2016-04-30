#coding:utf-8
#re.search函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回，如果字符串没有匹配，则返回None。
import re
f = open('d:\\file','r')
for line in f:
    m = re.search(r'(.*)unix',line)    
    if m:
        print m.group(0)
    
       
    
     
