#coding:utf8
import requests
import threading
payload = {'a': '7', 'b': '9'}
# r = requests.get("http://127.0.0.1:8000/get", params=payload)

def sayhello():
    r = requests.get("http://127.0.0.1:8000/get", params=payload)
    # print "hello world"
    global t  # Notice: use global variable!
    t = threading.Timer(2.0, sayhello)
    t.start()


t = threading.Timer(2.0, sayhello)  # 相隔2秒执行
t.start()