#coding:utf-8
#instance表示实例
from _pyio import __metaclass__

#定义中第一类的方式如下
#解析;类的名字后面跟上(object)，这其实是一种名为“继承”的类的操作，
#当前的类BB是以类object为上级的（object被称为父类），即BB是继承自类object的新类。

class BB(object):
    pass

bb = BB()
#print type(BB)
#print type(bb)

#另一种定义方法如下：
#在类的前面写上这么一句：__metaclass__ == type，然后定义类的时候，
#就不需要在名字后面写(object)了。

################################################################################
#self指的是类实例对象本身(注意：不是类本身)。self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
__metaclass__ = type
class person:
    def __init__(self,name):
        self.name = name
    
    def getname(self):
        return self.name
    def colour(self,color):
        print self.name,color


      
        