v11.py的脚本，如果我们改写ip地址或者改成不通的接口地址，会报错如下错误:

################################################
Traceback (most recent call last):
  File "D:/Pycharm/kk/Search_api???/11.py", line 9, in <module>
    html = urllib2.urlopen(url,post_data).read()
  File "D:\Python27\lib\urllib2.py", line 154, in urlopen
    return opener.open(url, data, timeout)
  File "D:\Python27\lib\urllib2.py", line 437, in open
    response = meth(req, response)
  File "D:\Python27\lib\urllib2.py", line 550, in http_response
    'http', request, response, code, msg, hdrs)
  File "D:\Python27\lib\urllib2.py", line 475, in error
    return self._call_chain(*args)
  File "D:\Python27\lib\urllib2.py", line 409, in _call_chain
    result = func(*args)
  File "D:\Python27\lib\urllib2.py", line 558, in http_error_default
    raise HTTPError(req.get_full_url(), code, msg, hdrs, fp)
urllib2.HTTPError: HTTP Error 404: Not Found

#################################################
但是我们只想要1和0的输出，所以错误并不是我们想要的 ，我们要避开错误提示，也就是要用到异常的处理.

改进脚本在v11以上.

