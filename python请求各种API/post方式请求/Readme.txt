POST��ʽ��

params = urllib.urlencode({'id': 8, 'name': 'jack', 'age': 25})
f = urllib.urlopen("http://localhost:18797/MailClient/test.aspx",params)
print f.read()
����ԭ��

urllib.urlopen(url[, data[, proxies]]) 
urllib2
������ϸ�Ķ���header����

httplib
��ײ������ǿ���http�������Ӧ