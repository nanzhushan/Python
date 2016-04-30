#coding:utf-8
from _pyio import __metaclass__
__metaclass__ = type

class Animal:
    def __init__(self,name=""):
        self.name = name

#定义说话的方法 ，也就是对象的行为       
    def talk(self):
        pass
    
##继承动物类
class Cat(Animal):
    def talk(self):
        print "maomi"

#狗类继承动物类
class Dog(Animal):
    def talk(self):
        print "woof"
        
#实例化动物类，方法
a = Animal()
a.talk()

c = Cat("missy")

#访问类的方法
c.talk()

d = Dog('rocky')
d.talk()


        
