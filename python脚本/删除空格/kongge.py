#coding:utf-8
#删除空格的第一种方法如下:
import re
b = "  x yz fdf  "
print b.replace(' ','')

#删除空格的方法第二种如下,用split断开再合上 
s = " x  y z  "
print "".join(s.split())

#只去两端的空格
c = "  dfd df  "
print c.strip('')

