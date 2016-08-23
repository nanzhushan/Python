#coding=utf-8
import threading
from time import ctime,sleep

def music(x):
    for i in range(2):
        print "I was listening to %s. %s" %(x,ctime())
        sleep(1)

def move(x):
    for i in range(2):
        print "I was at the %s! %s" %(x,ctime())
        sleep(5)



if __name__ == '__main__':
    music(u'爱情买卖')
    move(u'阿凡达')

    print "我都做完了 %s" %ctime()