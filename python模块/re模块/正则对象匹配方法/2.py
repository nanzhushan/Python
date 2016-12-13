#coding:utf-8
import re
#正则对象匹配方法
#2)groups([default])

#返回一个元组包含所有子组的匹配。

m = re.match(r"(\d+)\.(\d+)", "24.1632")
print m.groups()