#coding:utf-8
import re
#�������ƥ�䷽��
#5)span()
#����:  ���б���ʽ����ƥ��������ʼ�ͽ���ֵ

email = "knight@163_126.com" 
m = re.search(r"_126", email)
print m.span()