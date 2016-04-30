#coding:utf-8
#https://github.com/yorkoliu/pyauto
import os,sys
import time
import sys
import pycurl

URL="http://www.fang.com"
c = pycurl.Curl()            #创建一个curl对象
c.setopt(pycurl.URL, URL)     #定义请求的url常量
                
#连接超时时间,5秒
c.setopt(pycurl.CONNECTTIMEOUT, 5)

#下载超时时间,5秒
c.setopt(pycurl.TIMEOUT, 5)   #定义请求的超时时间
c.setopt(pycurl.FORBID_REUSE, 1)  #完成交互后强制断开连接,不重用
c.setopt(pycurl.MAXREDIRS, 1)    #指定http重定向的最大数为1
c.setopt(pycurl.NOPROGRESS, 1)   #屏蔽下载进度条
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt", "wb")
c.setopt(pycurl.WRITEHEADER, indexfile)
c.setopt(pycurl.WRITEDATA, indexfile)
try:
    c.perform()             #提交请求  
except Exception,e:
    print "connecion error:"+str(e)
    indexfile.close()
    c.close()
    sys.exit()

NAMELOOKUP_TIME =  c.getinfo(c.NAMELOOKUP_TIME)      #获取dns解析时间
CONNECT_TIME =  c.getinfo(c.CONNECT_TIME)               #获取建立的时间  
PRETRANSFER_TIME =   c.getinfo(c.PRETRANSFER_TIME)     
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)

TOTAL_TIME = c.getinfo(c.TOTAL_TIME)           #获取传输的总时间
HTTP_CODE =  c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD =  c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)            #获取http头部
SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)       #获取平均下载速度

print "HTTP状态码：%s" %(HTTP_CODE)
print "DNS解析时间：%.2f ms"%(NAMELOOKUP_TIME*1000)
print "建立连接时间：%.2f ms" %(CONNECT_TIME*1000)
print "准备传输时间：%.2f ms" %(PRETRANSFER_TIME*1000)
print "传输开始时间：%.2f ms" %(STARTTRANSFER_TIME*1000)
print "传输结束总时间：%.2f ms" %(TOTAL_TIME*1000)

print "下载数据包大小：%d bytes/s" %(SIZE_DOWNLOAD)
print "HTTP头部大小：%d byte" %(HEADER_SIZE)
print "平均下载速度：%d bytes/s" %(SPEED_DOWNLOAD)

indexfile.close()
c.close()