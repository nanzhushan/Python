#coding:utf-8
__metaclass__ = type

class Person:
    def __init__(self, name):
        self.name = name

    def getName(self):
        #return self.name
        return girl.name     #修改成这个样子，但是在编程实践中不要这么做。

girl = Person('canglaoshi')
name = girl.getName()
print name