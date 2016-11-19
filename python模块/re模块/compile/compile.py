#coding:utf-8
import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."
regex = re.compile(r'\w*oo\w*')
print regex.findall(text)   #查找所有包含'oo'的单词
print regex.sub(lambda m: '[' + m.group(0) + ']', text) #将字符串中含有'oo'的单词用[]括起来。