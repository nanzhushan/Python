#coding:utf-8
import re
#�������ƥ�䷽��
#6)span()
#����:  �����ַ�����ʼ�ͽ�������ֵ

email = "knight@163_126.com" 
m = re.search(r"_126", email)
print m.pos
print m.endpos