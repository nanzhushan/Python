import re
f =open('c:d.txt','r')
for i in f.readlines():
    t = re.compile('^\s.*\s$')
    m =re.match(t,i)
    if m:
        print m.group()
