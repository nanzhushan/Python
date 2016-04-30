#coding:utf8
#推荐使用新浪邮箱
import poplib
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mailto_list = '1093381395@qq.com'
mail_host = 'smtp.sina.cn'
mail_user = 'xxx'
mail_pass = 'xxx'
mail_postfix = 'sina.cn'

#邮件发送函数
def send_mail(to_list,sub,content):     #to_list：收件人；sub：主题；content：邮件内容
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"       #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='utf-8')      #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    s = smtplib.SMTP()
    s.connect(mail_host)  # 连接smtp服务器
    s.login(mail_user,mail_pass)  #登陆服务器
    s.sendmail(me, to_list, msg.as_string())  #发送邮件
    s.close()

zhengwen = "这是正文"
zhuti = "这是主题"
##发送邮件
send_mail(mailto_list,zhuti,zhengwen)


