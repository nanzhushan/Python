#coding:utf8
##方法一
t = "true"
a =  [12,4,6,88,9]
b = [12,3,6,88,99,4,6]

if set(b) > set(a):
    pass
else:
    t = "false"

print t


