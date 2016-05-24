#coding:utf8
import threading

def aa():
    print "这是aa的方法"

timer = threading.Timer(5,aa)
timer.start()