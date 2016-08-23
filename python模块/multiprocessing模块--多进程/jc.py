#coding:utf8
'''

使用进程池。它可以让你跑满多核CPU，而且使用方法非常简单。
注意要用apply_async，如果落下async，就变成阻塞版本了。
processes=2是最多并发进程数量。

'''
import multiprocessing
import time
def aa(msg):
    for i in xrange(15):
        print msg
        time.sleep(1)


if __name__=="__main__":
    pool = multiprocessing.Pool(processes=2)
    msg = "xxxxoooo"
    pool.apply_async(aa,(msg,))
    pool.close()
    pool.join()
