#coding:utf8
import time
import os
i = 0
count = 0

while (i < 6):
    i += 1
    count = 1
    if (count < 1):
        time.sleep(2)
        continue
    break

if (count < 1):
    print "重启进程...."

print "最后的进程值为:",count
print type(count)





