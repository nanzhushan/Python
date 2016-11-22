（1）实际上JSON就是Python字典的字符串表示，
但是字典作为一个复杂对象是无法直接传递,所以需要将其转换成字符串形式.
转换的过程也是一种序列化过程.

（2）
encoding：把一个Python对象编码转换成Json字符串
decoding：把Json格式字符串解码转换成Python对象

decoding: 解码
encoding: 编码


对于简单数据类型（string、unicode、int、float、list、tuple、dict），可以直接处理

（3）
j2.py用于输出最标准的json格式


（4）每次遇到json loads/dumps始终搞不清方向，总结如下 ：

json.dumps : dict转成str
json.loads:str转成dict
如此简单。

（5）JSON 函数

函数	程序库
encode	Python对象编码成JSON字符串表示

decode	解码JSON endoded的字符串转换成一个Python对象