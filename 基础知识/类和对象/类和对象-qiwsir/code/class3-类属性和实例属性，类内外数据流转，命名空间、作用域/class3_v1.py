#coding:utf-8
#object可以加也可以不加，新旧类的区别而已，没加的是新式类
#类前面如果有：__metaclass__ = type  表示另一种类的定义方法
class A():
    x = 7
    
print A()
# for循环报错
#for h in A():
#
#    print h

##类只有实例化后才可以用引用访问其中的属性和方法   
a = A()
print a.x
