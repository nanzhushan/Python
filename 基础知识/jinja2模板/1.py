#coding:utf8
from jinja2 import Template
a = "hello {{ name }}!  you are {{ sex }}"

tem = Template(a)
print tem.render(name='knight',sex='man')
