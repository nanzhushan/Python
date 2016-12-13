#coding:utf-8
#   1）(?=...)
import re
'''
正先行断言，匹配后面能匹配的表达式。
有两个re字符串，只想匹配regular中的：
r: 表示原生字符串，后面的东西就不需要转义

'''

## 匹配gular前面的两个字符
print re.findall(r"..(?=gular)", "A regular expression") 

## 匹配gular 后面的5个字符
print  re.findall(r"(?=gular).{5}", "A regular expression")