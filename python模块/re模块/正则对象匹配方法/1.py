#coding:utf-8
#�������ƥ�䷽��
#1)group([group1,....])

import re
m = re.match(r'(\w+) (\w+)', 'hello world')
print m.group(0)  #ȫ����ƥ��
print m.group(1)   #��һ����������
print m.group(2)    #�ڶ�����������

print m.group(1,2)

a = re.match(r"(..)+", "a1b2c3")
print a.group(1)