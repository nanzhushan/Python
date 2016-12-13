#coding:utf-8
import re
#正则对象匹配方法
#6)span()
#例如:  返回字符串开始和结束索引值

email = "knight@163_126.com" 
m = re.search(r"_126", email)
print m.pos
print m.endpos