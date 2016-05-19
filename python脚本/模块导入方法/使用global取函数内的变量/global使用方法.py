#coding:utf8
def a():
    global bb
    bb = 5
    print "hello"

a()  #执行函数，常用登录入口，从而赋值

def cc():
    print bb


cc()   #调用函数