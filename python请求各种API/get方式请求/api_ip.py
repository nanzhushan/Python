#coding:utf8
#通过淘宝的ip库查询ip地址归属地

import requests
lastip = '114.215.199.94'
r = requests.get('http://ip.taobao.com/service/getIpInfo.php')

# print r
payload = {'ip':lastip}
r = requests.get("http://ip.taobao.com/service/getIpInfo.php",params=payload)
print(r.url)
print r.text.decode('unicode-escape')

