Request类

正如前面区别urllib和urllib2所讲，利用urllib2模块可以建立一个Request对象。方法就是：

>>> req = urllib2.Request("http://zabbix.knight.ren")
建立了Request对象之后，它的最直接应用就是可以作为urlopen()方法的参数

>>> response = urllib2.urlopen(req)
>>> page = response.read()
>>> print page
因为与前面的urllib.open("http://zabbix.knight.ren")结果一样，就不浪费篇幅了。

但是，如果Request对象仅仅局限于此，似乎还没有什么太大的优势。因为刚才的访问仅仅是满足以get方式请求页面，并建立类文件对象。如果是通过post向某地址提交数据，也可以建立Request对象。

import urllib    
import urllib2    

url = 'http://zabbix.knight.ren/register.py'    

values = {'name' : 'qiwsir',    
          'location' : 'China',    
          'language' : 'Python' }    

data = urllib.urlencode(values)     # 编码  
req = urllib2.Request(url, data)    # 发送请求同时传data表单  
response = urllib2.urlopen(req)     #接受反馈的信息  
the_page = response.read()          #读取反馈的内容
注意，读者不能照抄上面的程序，然后运行代码。因为那个url中没有相应的接受客户端post上去的data的程序文件。上面的代码只是以一个例子来显示Request对象的另外一个用途，还有就是在这个例子中是以post方式提交数据。

在网站中，有的会通过User-Agent来判断访问者是浏览器还是别的程序，如果通过别的程序访问，它有可能拒绝。这时候，我们编写程序去访问，就要设置headers了。设置方法是：

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
然后重新建立Request对象：

req = urllib2.Request(url, data, headers)    
再用urlopen()方法访问：

response = urllib2.urlopen(req) 
除了上面演示之外，urllib2模块的东西还很多，比如还可以:

设置HTTP Proxy
设置Timeout值
自动redirect
处理cookie
