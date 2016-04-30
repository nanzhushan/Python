#coding=utf-8
'''
创建文件
author=knight
'''
import os
import time

def nsfile(s):
    '''The number of new expected documents'''
    #判断文件夹是否存在，如果不存在则创建
    b = os.path.exists("E:\\testfile\\")
    if b:
        print "File Exist!"
    else:
        os.mkdir("E:\\testfile\\")
    #生成文件
    for i in range(1,s+1):
        localTime = time.strftime("%Y-%m%d-%H%M%S",time.localtime())
        #print localtime
        filename = "E:\\testfile\\"+localTime+".txt"
        #a:以追加模式打开（必要时可以创建）append;b:表示二进制
        f = open(filename,'ab')
        testnote = '测试文件'
        f.write(testnote)
        f.close()
        #输出第几个文件和对应的文件名称
        print "file"+" "+str(i)+":"+str(localTime)+".txt"
        time.sleep(1)
    print "All done"
    time.sleep(1)

if __name__ == '__main__':
    s = input("请输入需要生成的文件数：")
    nsfile(s)