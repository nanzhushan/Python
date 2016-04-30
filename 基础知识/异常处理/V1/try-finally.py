#coding:utf-8
'''
try-finally 语句无论是否发生异常都将执行最后的代码。

try:
<语句>
finally:
<语句>    #退出try时总会执行
raise

'''
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print "Error: can\'t find file or read data"
