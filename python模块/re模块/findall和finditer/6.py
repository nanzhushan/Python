#coding:utf-8
import re

#得到所有匹配的数字
text = "a1b2c3"
print re.findall(r'\d+', text)

for m in re.finditer(r'\d+', text):
	print m.group()