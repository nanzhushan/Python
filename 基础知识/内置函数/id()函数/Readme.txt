说明;
本函数是返回对象object的标识符，标识符类型为整数，在同一个时间里所有对象的标识符是唯一的，如果在不同生命周期的对象有可能有相同的标识符。比如创建对象A之后，再删除A，再创建对象B，对象A与对象B可能有相同的标识符。在CPython里的实现算法是直接返回对象所在内存地址。


>>> print id(5)
30765448
>>> print id(6)
30765424
>>> help(id)
Help on built-in function id in module __builtin__:

id(...)
    id(object) -> integer

    Return the identity of an object.  This is guaranteed to be unique among
    simultaneously existing objects.  (Hint: it's the object's memory address.)
