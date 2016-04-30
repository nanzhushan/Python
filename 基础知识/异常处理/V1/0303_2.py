#coding:utf-8
import urllib
url = 'http://127.0.0.1/gongji/login/login.html'

#定义字典
data = {'name':'knight',
        'password':'knight'
        }

#编码成json格式
post_data = urllib.urlencode(data)
#print post_data
#print type(post_data)
#print data
#print type(data)
#f  = urllib.urlopen(url, post_data)
#print f.read()
#print f.info()             #打印头部

#使用try语句来验证程序是否执行成功  .类似于shell里的 $?。
try :
    f  = urllib.urlopen(url, post_data)
except:
    print "登录失败"
else:
    print "登录成功"
    

    
    



