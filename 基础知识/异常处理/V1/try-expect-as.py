#/usr/bin/env python
#coding:utf8
# as : 定义异常实例(except IOError as e)
try:
	print "try try try"

except Exception as e:
	print "接受异常，并把这个异常储存起来，方便以后打出到文件或者其他地方",e