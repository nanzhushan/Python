#coding:utf-8
import re
#正则对象匹配方法
#5)span()
#例如:  以列表形式返回匹配索引开始和结束值

email = "knight@163_126.com" 
m = re.search(r"_126", email)
print m.span()