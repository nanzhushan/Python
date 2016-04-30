环境:centos6.5_x64

yum install httpd -y

配置文件请看如下:




配置完成之后在:
ls /var/www/cgi-bin/
chmod 755 /var/www/cgi-bin/* 

##cgi方式访问脚本
curl http://192.168.2.101/cgi-bin/tt.py