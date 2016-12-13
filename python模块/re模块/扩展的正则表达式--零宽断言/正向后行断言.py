#coding:utf-8
import re
'''
正向后行断言，匹配前面能匹配表达式。
只想匹配单词里的re，排除开头的re：
在re前面有一个或多个字符，所以叫后行断言，
正则匹配是从前向后，当遇到断言时，会再向字符串前端检测已扫描的字符，
相对于扫描方向是向后的。

'''
print re.findall(r"(?<=\w)re", "A regular expression")
print re.findall(r"(?<=\w)re.", "A regular expression") 
