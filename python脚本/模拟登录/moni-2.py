#coding:utf8
import json
import requests

##模拟登陆简化版,真的好简单 用request真是利器

payload = {'name': 'knight', 'password': 'knight'}
r = requests.post("http://127.0.0.1/login1.php", data=payload)
print r.text

