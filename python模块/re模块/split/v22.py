#coding:utf8
import re

##对于 str.split():
print 'hello,world'.split()   #第一次打印
print 'hello,world'.split(',')   # 第二次打印

#对于re.split():

#re.split()方法可以使用正则表达式匹配，具体用法如下
print re.split(r'\W+','hello,world') #第三次打印
print re.split(r'\W+','hello,world')[1]


#如果使用带括号的正则表达式则可以将正则表达式匹配的内容也添加到列表内，例如
print re.split(r'(\W+)','hello,world')