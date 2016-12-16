(1)
https://github.com/qiwsir/StarterLearningPython/blob/master/216.md

举个例子：

ZeroDivisionError

>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero

很明显分母不能为0，会抛出异常，在程序设计中要处理这个异常，异常发生时候给用户友好
提示而不是抛出异常。


(2)与Python异常相关的关键字：

关键字          关键字说明
raise           抛出/引发异常
try/except      捕获异常并处理
pass            忽略异常
as              定义异常实例(except IOError as e)
finally         无论是否出现异常，都执行的代码
else            如果try中的语句没有引发异常，则执行else中的语句