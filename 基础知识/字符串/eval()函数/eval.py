#!/usr/bin/env python
#coding:utf8

#eval函数将字符串当成有效Python表达式来求值，并返回计算结果
x = 1
print eval('x+1')
print eval('x==1')
print "###################"
#与之对应的repr函数，它能够将Python的变量和表达式转换为字符串表示
a = repr(x==1)
print a
print type(a)

print repr(x+1)