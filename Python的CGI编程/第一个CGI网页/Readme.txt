һ:
CGI���ǿ���ͨ��Python��д�����Զ��ڵ�ҳ��web�������ʹ��cgi��ʽ����

ʲô��CGI 
1. ���壺 
CGI(Common Gateway Interface)��HTTP����������Ļ��������� 
�ϵĳ�����С���̸����һ�ֹ��ߣ������������������������ϡ�

CGI�����裺 
��ͨ��Internet���û������͵��������� 
�Ʒ����������û����󲢽���CGI������ 
��CGI����Ѵ��������͸��������� 
�ȷ������ѽ���ͻص��û��� 
(5)CGI���������Python�ű���PERL�ű���SHELL�ű���C����C++����ȡ�


��װ����:
�����ÿ�ܣ�������Django��������http��cgi��ʽ����python�ļ���
��װ����:
yum install httpd -y

��װ�õ�httpĬ����֧��cgi�ˡ�(ֻҪ�������ط�)

(1)��http.conf������  :
Options +ExecCGI

(2)
�� AddHandler  �к������.py
AddHandler cgi-script .cgi .py .pl

(3)
cgi����վ��Ŀ¼��:/var/www/cgi-bin
cd /var/www/cgi-bin
chmod 755 *

�����ļ�������755 Ȩ��

���·�����Դ���ļ���

���ʷ�ʽ: http://192.168.2.101/cgi-bin/tt.py