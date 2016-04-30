#coding:utf-8
#打印指定行数
import linecache

file=open('d:\\1.txt','r')
linecount=len(file.readlines())
dd1 = linecache.getline('d:\\1.txt',1)
dd2 = linecache.getline('d:\\1.txt',2)
print dd1
print dd2