#coding:utf-8
import re
'''
正先行断言，匹配后面能匹配的表达式。
有两个re字符串，只想匹配regular中的：
'''


print re.findall(r"..(?=gular)", "A regular expression") 

print  re.findall(r"(?=gular).{5}", "A regular expression")