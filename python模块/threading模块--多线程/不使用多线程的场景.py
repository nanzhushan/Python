#coding:utf8
from time import ctime,sleep

def music():
    for i in range(2):
        print "我想要听音乐 %s" %ctime()
        sleep(1)

def move():
    for i in range(2):
        print "我想要看电视! %s" %ctime()
        sleep(5)

if __name__ == '__main__':
    music()
    move()
    print "====================================="
    print "我都看完了 %s" %ctime()