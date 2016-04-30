#coding:utf-8
'''
笑话如下：
某软件公司老板，号称自己懂技术。一次有一个项目要交付给客户，
但是他有不想让客户知道实现某些功能的代码，
但是交付的时候要给人家代码的。于是该老板就告诉程序员，
“你们把那部分核心代码封装一下”。程序员听了之后，迷茫了
'''
from _pyio import __metaclass__

__metaclass__= type

class Protectme:
    def __init__(self):
        self.me = 'knight'
        self.__name = 'zhoulong'
    
    def __python(self):
        print "i am study py"
    
    def code(self):
        print "which language do you like"
        self.__python()

##运行报错    
#"AttributeError: 'Protectme' object has no attribute '__name'",对象没有那个__name属性
#也就是在类的外面无法调用
if __name__== "__main__":    
    p = Protectme()
    print p.me
    print p.__name
    

    
    
        
      
        
    