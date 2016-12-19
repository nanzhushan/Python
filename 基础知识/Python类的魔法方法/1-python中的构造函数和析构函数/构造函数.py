#!/usr/bin/env python
#coding:utf8
"""
构造函数：
用于初始化类的内容部状态，Python提供的构造函数式 __init__();
当该类被实例化的时候就会执行该函数。
那么我们就可以把要先初始化的属性放到这个函数里面
"""
class tt(object):   #object 类就是基类
    def __init__(self):
        print "AAA AAAA"
    def my(self):
        print "CCCC CCCC"
obj = tt()
obj.my()





