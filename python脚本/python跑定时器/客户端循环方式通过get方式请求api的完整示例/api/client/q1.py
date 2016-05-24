#coding:utf8
import requests
payload = {'a': '7', 'b': '9'}
r = requests.get("http://127.0.0.1:8000/get", params=payload)
# print r.text