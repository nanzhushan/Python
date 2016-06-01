#!/usr/bin/python
#coding:utf8
import tail

def print_line(txt):
    print(txt)

t = tail.Tail('/root/loglog')
t.register_callback(print_line)
t.follow(s=1)  ##读取时间
