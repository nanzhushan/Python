#!/usr/bin/env python
#coding:utf8

def aa():
    return "这是aa函数"


def bb():
    return "bb函数...."

print "这是文件的主程序...."

#只有执行这个文件的时候，才执行if里的语句,如果只是被别人调用不执行里面的语句
if __name__ == "__main__":
    print "这是文件的主程序...."
    bb()

