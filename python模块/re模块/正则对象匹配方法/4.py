#coding:utf-8
import re
#�������ƥ�䷽��
#4)start()��end()
#����: ȥ���ʼ���ַ��ĳ�ַ�

email = "knight@163_126.com" 
m = re.search(r"_126", email)
print email[:m.start()] + email[m.end():]
