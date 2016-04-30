#coding:utf-8

class Employee:
#有员工的基类
    empCount = 0

    def __init__(self, name, salary):        
        self.name = name
        self.salary = salary
     #  Employee.empCount += 1
        Employee.empCount = Employee.empCount +1
        
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name,  ", Salary: ", self.salary

#创建 Employee 类的第一个对象
emp1 = Employee("knight", 2000)

#创建 Employee 类的第二个对象
emp2 = Employee("monica", 5000)

#访问属性
#您可以使用点(.)来访问对象的属性。也就是定义的 "对象+方法"，来访问属性，使用如下类的名称访问类变量:
emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount