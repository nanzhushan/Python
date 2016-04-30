#coding:utf8
cc = 6
ee = "hehe"
aa = 5

try:
    dd = cc/0
except ZeroDivisionError:
    print "发生ZeroDivisionError，也就是发生分母是0的异常  输出这个except..."

except TypeError:
    print "发生另外一个异常，执行这个 except语句"