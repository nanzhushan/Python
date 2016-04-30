#coding:utf-8
#使用的是第二种定义类的方法
__metaclass__ = type             #新式类

class Person:                    #创建类
    def __init__(self, name):    #构造函数
        self.name = name

    def getName(self):           #类中的方法（函数）
        return self.name

    def color(self, color):
        print "%s is %s" % (self.name, color)

girl = Person('canglaoshi')      #实例化
name = girl.getName()            #调用方法（函数） 
print "the person's name is: ", name

girl.color("white")              #调用color方法（函数）

print "------"
print girl.name                  #实例的属性