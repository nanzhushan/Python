#coding:utf8
#  echo "xxyyb2cde" | grep -oP '(?<=b)..'
#下面的内容和shell等价
import re 

str = "xxyyb2cde"
print re.findall(r"..(?=b)",str)    #不包含b

print re.findall(r"..(?<=b)",str)    ##包含b

print re.findall(r"(?<=b).{3}",str)   #不包含b

print re.findall(r"(?=b).{3}",str)   #包含b

