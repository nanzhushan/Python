#coding:utf-8
#  2）(?!...)
import re
'''
负先行断言，匹配后面不能匹配表达式。
只想匹配expression中的re字符串，排除掉regular单词：
'''

print re.findall(r"re(?!g)", "A regular expression") 
print re.findall(r"re(?!g).{5}", "A regular expression")