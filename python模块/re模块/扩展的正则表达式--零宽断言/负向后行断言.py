#coding:utf-8
#   4）(?<!...)
import re
'''
负向后行断言，匹配前面不能匹配的表达式。

'''

print re.findall(r"(?<!\w)re", "A regular expression") 
print re.findall(r"(?<!\w)re.", "A regular expression")