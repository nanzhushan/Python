#coding:utf-8
from lxml import  etree
import requests

html = requests.get('http://127.0.0.1/xpath/test_regular.html')
#编码成utf-8 格式，不然会是中文乱码
html.encoding = 'utf8'
html1 = html.text
aa = etree.HTML(html1)
bb = aa.xpath('//ul[@id="useful"]/li/text()')

for i in bb:
    print i