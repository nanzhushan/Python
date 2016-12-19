#!/usr/bin/env python
#coding:utf8
"""
下面的“__del__”就是一个析构函数了，当使用del 删除对象时，会调用他本身的析构函数，
另外当对象在某个作用域中调用完毕，在跳出其作用域的同时析构函数也会被调用一次，这样可以用来释放内存空间。

注意:   __del__()是可选的，如果不提供，则Python 会在后台提供默认析构函数
如果要显式的调用析构函数，可以使用del关键字，方式如右边： def 对象名

"""

class tt(object):   #object 类就是基类
    def my(self):
        print "CCCC CCCC"
    def __del__(self):
        print "\033[33m 这是del的析构函数...\033[0m"

obj = tt()
obj.my()
del obj

