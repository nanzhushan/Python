#coding:utf-8
import re

# ̰��ƥ��
print re.findall(r"<div>.*</div>", "<div>a</div><div>b</div><div>c</div>")

# ��̰��ƥ��
print re.findall(r"<div>.*?</div>", "<div>a</div><div>b</div><div>c</div>")

print re.findall(r"a(\d+)", "a123b") 

# ����ұ����޶�����̰��ʧЧ
print re.findall(r"a(\d+)b", "a123b")  
print re.findall(r"a(\d+?)b", "a123b")  