#coding:utf-8
import re

# 贪婪匹配
print re.findall(r"<div>.*</div>", "<div>a</div><div>b</div><div>c</div>")

# 非贪婪匹配
print re.findall(r"<div>.*?</div>", "<div>a</div><div>b</div><div>c</div>")

print re.findall(r"a(\d+)", "a123b") 

# 如果右边有限定，非贪婪失效
print re.findall(r"a(\d+)b", "a123b")  
print re.findall(r"a(\d+?)b", "a123b")  