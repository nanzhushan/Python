# coding=utf-8
'''
从运行情况看，当在第二个数，即除数为0时，程序并没有因为这个错误而停止，
而是给用户一个友好的提示，让用户有机会改正错误。
这完全得益于程序中“处理异常”的设置，如果没有“处理异常”，异常出现，就会导致程序终止。

处理异常的方式之一，使用try...except...。

对于上述程序，只看try和except部分，如果没有异常发生，except子句在try语句执行之后被忽略；如果try子句中有异常可，该部分的其它语句被忽略，直接跳到except部分，执行其后面指定的异常类型及其子句。

except后面也可以没有任何异常类型，即无异常参数。如果这样，不论try部分发生什么异常，都会执行except。

'''

while 1:
    print "this is a division program."
    c = raw_input("input 'c' continue, otherwise logout:")
    if c == 'c':
        a = raw_input("first number:")
        b = raw_input("second number:")
        try:
            print float(a)/float(b)
            print "*************************"
        except ZeroDivisionError:
            print "The second number can't be zero!"
            print "*************************"
    else:
        break