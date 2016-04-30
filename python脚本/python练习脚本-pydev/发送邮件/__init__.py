#coding:utf-8
'''
fuction:文本形式发送邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = 'hb_monitor@189.cn'
receiver = '624867243@qq.com'
subject = 'tttttt'
smtpserver = 'smtp.189.cn'
username = 'hb_monitor'
password = 'xxxx'

msg = MIMEText('亲爱的，你好','text','utf-8')  #中文需参数‘utf-8’，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8') 

smtp = smtplib.SMTP()  
smtp.connect('smtp.189.cn')  
smtp.login(username, password) 
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()