#coding:utf8
'''
在python中，我理解的simplejson模块就是主要用于将python数据类型转换为json类型。

json有两种结构：
1，名称/值 的形式。在python中就是字典的结构
2，值的有序列表。简单点就是数组结构，在python中类似于列表结构

(1)名称/值 这里不做解释

(2)，对象时一个数组，数组是值（value）的有序集合。一个数组以“[”（左中括号）开始，“]”（右中括号）结束。值之间使用“,”（逗号）分隔。
eg:["cynthia","is testing","age",18,["reading",18]]


'''

# simplejson的主要函数：

# dumps():将python字典json化
import simplejson

a = {"name":"kngiht","sex":"man"}
# print type(a)
c = simplejson.dumps(a)
print type(c)
print c

##解码成python数据类型
c1 = simplejson.loads(c)
print type(c1)
print c1


