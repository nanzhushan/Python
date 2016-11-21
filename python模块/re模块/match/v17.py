#coding:utf8
import re
#使用match函数返回一个match对象
m = re.match('^[\w]{3}','abcdf')

#使用group方法输出所有匹配的字符串
if m:
    print m.group()

#或者使用如下：
print re.match('foo','food').group()