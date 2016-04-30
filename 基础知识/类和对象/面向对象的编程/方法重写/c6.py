#coding:utf-8
#方法重写
class Parent:  #定义父类
    def myMethod(self):
        print ' 调用父类方法'

class Child(Parent):   #定义子类，继承父类
    def myMethod(self):      #重写父类的myMethod方法
        print '调用子类的方法'


c = Child()       #子类实例
c.myMethod()
