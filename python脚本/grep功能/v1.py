#coding:utf8
import sys,os
f = open("c:\\aa.txt",'r')
a =f.readlines()
print len(a)
# print a[6]
print a[3:8]
for i in a[3:8]:
    print i