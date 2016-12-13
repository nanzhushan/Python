#coding:utf-8
import re
#正则对象匹配方法
#4)start()和end()
#例如: 去掉邮件地址的某字符

email = "knight@163_126.com" 
m = re.search(r"_126", email)
print email[:m.start()] + email[m.end():]
