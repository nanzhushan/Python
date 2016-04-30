#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
可以使用中文标题和正文
'''

import smtplib
from email.MIMEText import MIMEText
from email.Header import Header

#################################################
# Setting mail-server, etc
mail_host="smtp.189.cn"
mail_user="tom"
mail_pass="123456"
mail_postfix="189.cn"

#################################################
# sub-function
def send_mail(to_list, sub, content):
  me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
#  msg = MIMEText(content)
  msg = MIMEText(content,_subtype='plain',_charset='utf-8')
  msg['Subject'] = sub
  msg['From'] = me
  msg['To'] = ";".join(to_list)

  try:
    s = smtplib.SMTP()
    s.connect(mail_host)
    s.login(mail_user, mail_pass)
    s.sendmail(me, to_list, msg.as_string())
    s.close()
    return True
  except Exception, e:
    print str(e)
    return False

#################################################
# Main process
if __name__ == "__main__":
  # 
  mailto_list=["1093781365@qq.com","18058049723@189.cn"]

  if send_mail(mailto_list, "标题", "正文"):
    print "Send success!"
  else:
    print "Send failed!"

# END
