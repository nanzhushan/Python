#coding:utf8
import re
r1 = re.compile('world')
if r1.match('helloworld'):
    print "match sucess"
else:
    print "match fails"

if r1.search('helloworld'):
    print "search sucess"
else:
    print "search fails"