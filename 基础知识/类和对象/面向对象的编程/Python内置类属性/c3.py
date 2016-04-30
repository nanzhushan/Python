#coding:utf-8

class Employee:
    #所有员工的基类
    empCount = 0

    def __init__(self, name, salary):        
        self.name = name
        self.salary = salary
        Employee.empCount += 1
   
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name,  ", Salary: ", self.salary

print "Employee.__doc__:", Employee.__doc__    #文档字符串
print "Employee.__name__:", Employee.__name__    #类名
print "Employee.__module__:", Employee.__module__    #类定义所在的模块
print "Employee.__bases__:", Employee.__bases__      #类的所有父类构成元素
print "Employee.__dict__:", Employee.__dict__   #类的属性