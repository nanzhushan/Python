#coding:utf8
import urllib
import urllib2
print "downloading with urllib"
url = 'http://192.168.30.12:8081/nexus/content/repositories/android/common/toastutils-lib/1.0.0/toastutils-lib-1.0.0.aar'
print "downloading with urllib"
urllib.urlretrieve(url, "d:\\toastutils-lib-1.0.0.aar")