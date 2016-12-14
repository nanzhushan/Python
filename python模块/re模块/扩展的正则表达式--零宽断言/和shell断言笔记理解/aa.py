#coding:utf8
#  echo "b2cde" | grep -oP '(?<=b)..'
#下面的内容和shell等价
import re 

str = "b2cde"
print re.findall(r"(?<=b)...",str)     

