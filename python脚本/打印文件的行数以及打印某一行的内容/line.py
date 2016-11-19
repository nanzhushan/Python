#coding:utf8
#读取多行内容
import linecache
line = linecache.getlines("c:\\d.txt")
print line
print line[1:4]
print line[1],line[3]

