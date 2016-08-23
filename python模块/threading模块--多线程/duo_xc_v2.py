#coding:utf8
'''
科技在发展，时代在进步，
我们的CPU也越来越快，CPU抱怨，
P大点事儿占了我一定的时间，其实我同时干多个活都没问题的；
于是，操作系统就进入了多任务时代。
我们听着音乐吃着火锅的不在是梦想。
参考链接:http://www.cnblogs.com/fnng/p/3670789.html

'''
import threading
from time import ctime,sleep

################

def music(func):
    for i in range(2):
        print "I was listening to %s. %s" %(func,ctime())
        sleep(1)

def move(func):
    for i in range(2):
        print "I was at the %s! %s" %(func,ctime())
        sleep(5)

#创建了threads数组，创建线程t1,使用threading.Thread()方法，
# 在这个方法中调用music方法target=music，args方法对music进行传参。 把创建好的线程t1装到threads数组中。
threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)

#接着以同样的方式创建线程t2，并把t2也装到threads数组。
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)


##原理：定义两个线程然后加入列表，使用setDaemon（守护进程）启动

#etDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，
# 如果不设置为守护线程程序会被无限挂起。子线程启动后，
# 父线程也继续执行下去，当父线程执行完最后一条语句print "我都看完了 %s" %ctime()后，
# 没有等待子线程，直接就退出了，同时子线程也一同结束。
#start()  开始线程活动

if __name__ == '__main__':
    t1.setDaemon(True)
    t2.setDaemon(True)

    t1.start()
    t2.start()
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()

    print "我都看完了 %s" %ctime()

