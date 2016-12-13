#coding:utf-8
#  2）(?!...)
import re
'''
负先行断言，匹配后面不能匹配表达式。
只想匹配expression中的re字符串，排除掉regular单词：
'''

# 匹配re字符串，排除掉g后面的单词内容
print re.findall(r"re(?!g)", "A regular expression") 


# 匹配re字符串，并且 re后面不是g开头，的5个字符
print re.findall(r"re(?!g).{5}", "A aagular expreccionddd")