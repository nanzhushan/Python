#coding:utf8
#使用python自动访问网页的程序
import webbrowser as web
import os

for i in  range(1,5):
    print i
    web.open_new_tab('www.baidu.com')

print os.system('taskkill  /f /im iexplore.exe')