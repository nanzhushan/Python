一:
CGI就是可以通过Python编写，所以对于单页的web程序可以使用cgi方式发布

什么是CGI 
1. 定义： 
CGI(Common Gateway Interface)是HTTP服务器与你的或其它机器 
上的程序进行“交谈”的一种工具，其程序须运行在网络服务器上。

CGI处理步骤： 
⑴通过Internet把用户请求送到服务器。 
⑵服务器接收用户请求并交给CGI程序处理。 
⑶CGI程序把处理结果传送给服务器。 
⑷服务器把结果送回到用户。 
(5)CGI程序可以是Python脚本，PERL脚本，SHELL脚本，C或者C++程序等。


安装部署:
不想用框架，不想用Django，可以用http的cgi方式运行python文件。
安装部署:
yum install httpd -y

安装好的http默认是支持cgi了。(只要改两处地方)

(1)在http.conf最后加上  :
Options +ExecCGI

(2)
在 AddHandler  中后面加上.py
AddHandler cgi-script .cgi .py .pl

(3)
cgi的网站根目录是:/var/www/cgi-bin
cd /var/www/cgi-bin
chmod 755 *

所有文件必须是755 权限

以下奉献上源码文件：

访问方式: http://192.168.2.101/cgi-bin/tt.py