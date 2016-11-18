#coding:utf8
#官方文档: https://docs.python.org/2/library/configparser.html
import ConfigParser
conf = ConfigParser.ConfigParser()

#读取配置文件
# conf.read("c:\\test.conf")

conf.read("test.conf")
name = conf.get("man","name")
print name

#获取所有的section
sections = conf.sections()
print sections

# 获取制定的section的option
options=conf.options("man")
print options
#获取制定的section的键值对
kvs = conf.items("man")
print kvs

#制定section,option读取值
age = conf.get("man","age")
print age
name = conf.get("man","name")
print "第一个section的名字是%s." %(name)