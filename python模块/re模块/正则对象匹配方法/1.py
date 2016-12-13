#coding:utf-8
#正则对象匹配方法
#1)group([group1,....])

import re
m = re.match(r'(\w+) (\w+)', 'hello world')
print m.group(0)  #全部组匹配
print m.group(1)   #第一个括号子组
print m.group(2)    #第二个括号子组

print m.group(1,2)

a = re.match(r"(..)+", "a1b2c3")
print a.group(1)