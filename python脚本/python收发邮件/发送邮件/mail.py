#coding:utf8
# 发送邮件，html或者文本形式的邮件
import poplib
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mailto_list = '1093381395@qq.com'
mail_host = 'smtp.189.cn'
mail_user = 'hb_monitor'
mail_pass = 'xxxxx'
mail_postfix = '189.cn'

def send_mail(to_list,sub,content):     #to_list：收件人；sub：主题；content：邮件内容
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"       #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='utf-8')      #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  # 连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    #if send_mail(mailto_list,"hello","<a href='http://www.baidu.com'>baidu</a>"):  #html格式
    if send_mail(mailto_list,"hello","百度"):                 #文本格式

        print "发送成功"
    else:
        print "发送失败"