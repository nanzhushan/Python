#coding:utf-8
import re
#�������ƥ�䷽��
#3)groupdict([default])

#��������������Ϊ����ƥ������Ϊֵ���ֵ䡣

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "hello world")
print m.groupdict()