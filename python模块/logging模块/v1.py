#coding:utf8
import logging

#创建一个logger
logger = logging.getLogger('mylogger')
#设置日志的级别
logger.setLevel(logging.DEBUG)

#创建一个handler,用于写入日志文件
fh=logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)    #debug日志级别写入文件
#定义handler的输出格式
fomatter= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#写入文件以这种格式写入
fh.setFormatter(fomatter)


#给logger添加handler
logger.addHandler(fh)

#记录一条日志
logger.info('football')

