#coding:utf-8
import re
#�������ƥ�䷽��
#2)groups([default])

#����һ��Ԫ��������������ƥ�䡣

m = re.match(r"(\d+)\.(\d+)", "24.1632")
print m.groups()