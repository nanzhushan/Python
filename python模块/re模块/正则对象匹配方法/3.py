#coding:utf-8
import re
#正则对象匹配方法
#3)groupdict([default])

#返回子组名字作为键，匹配结果作为值的字典。

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "hello world")
print m.groupdict()