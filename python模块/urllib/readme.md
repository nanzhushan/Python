Request��

����ǰ������urllib��urllib2����������urllib2ģ����Խ���һ��Request���󡣷������ǣ�

>>> req = urllib2.Request("http://zabbix.knight.ren")
������Request����֮��������ֱ��Ӧ�þ��ǿ�����Ϊurlopen()�����Ĳ���

>>> response = urllib2.urlopen(req)
>>> page = response.read()
>>> print page
��Ϊ��ǰ���urllib.open("http://zabbix.knight.ren")���һ�����Ͳ��˷�ƪ���ˡ�

���ǣ����Request������������ڴˣ��ƺ���û��ʲô̫������ơ���Ϊ�ղŵķ��ʽ�����������get��ʽ����ҳ�棬���������ļ����������ͨ��post��ĳ��ַ�ύ���ݣ�Ҳ���Խ���Request����

import urllib    
import urllib2    

url = 'http://zabbix.knight.ren/register.py'    

values = {'name' : 'qiwsir',    
          'location' : 'China',    
          'language' : 'Python' }    

data = urllib.urlencode(values)     # ����  
req = urllib2.Request(url, data)    # ��������ͬʱ��data��  
response = urllib2.urlopen(req)     #���ܷ�������Ϣ  
the_page = response.read()          #��ȡ����������
ע�⣬���߲����ճ�����ĳ���Ȼ�����д��롣��Ϊ�Ǹ�url��û����Ӧ�Ľ��ܿͻ���post��ȥ��data�ĳ����ļ�������Ĵ���ֻ����һ����������ʾRequest���������һ����;�����о������������������post��ʽ�ύ���ݡ�

����վ�У��еĻ�ͨ��User-Agent���жϷ���������������Ǳ�ĳ������ͨ����ĳ�����ʣ����п��ܾܾ�����ʱ�����Ǳ�д����ȥ���ʣ���Ҫ����headers�ˡ����÷����ǣ�

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
Ȼ�����½���Request����

req = urllib2.Request(url, data, headers)    
����urlopen()�������ʣ�

response = urllib2.urlopen(req) 
����������ʾ֮�⣬urllib2ģ��Ķ������ܶ࣬���绹����:

����HTTP Proxy
����Timeoutֵ
�Զ�redirect
����cookie
