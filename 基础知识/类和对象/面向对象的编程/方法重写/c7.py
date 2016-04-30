#coding:utf-8
#运算符从重写（重载）
class Car:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return 'Car (%d, %d)' % (self.a, self.b)
    def __add__(self,other):
        return Car(self.a + other.a, self.b + other.b)
    

v1 = Car(2,10)
v2 = Car(5,-2)

print "结果是Car(2+5,10-2):",v1 + v2