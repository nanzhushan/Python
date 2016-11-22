#coding:utf8
#默认异常处理器
s = "hello girl"

try:
    print s[100]


#程序执行到第2句时发现try语句，进入try语句块执行，发生异常，回到try语句层，寻找后面是否有except语句。
# 找到except语句后，会调用这个自定义的异常处理器。except将异常处理完毕后，程序继续往下执行。
except:
    print "错误"


print "继续"
