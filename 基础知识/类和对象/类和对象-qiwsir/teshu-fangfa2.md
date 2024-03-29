>所以，我们不丧胆。外体虽然毁坏，内心却一天新似一天。我们这至暂至轻的苦楚，要为我们成就极重无比永远的荣耀。原来我们不是顾念所见的，乃是顾念所不见的，因为所见的是暂时的，所不见的是永远的。(2 CORINTHIANS 4:16-18)

#特殊方法(2)

书接上回，不管是实例还是类，都用`__dict__`来存储属性和方法，可以笼统地把属性和方法称为成员或者特性，一句话概括，就是`__dict__`存储对象成员。但，有时候访问的对象成员没有存在其中，就是这样：

    >>> class A(object):
    ...     pass
    ... 
    >>> a = A()
    >>> a.x
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'A' object has no attribute 'x'

`x`不是实例的成员，用`a.x`访问，就出错了，并且错误提示中报告了原因：“'A' object has no attribute 'x'”

在很多情况下，这种报错是足够的了。但是，在某种我现在还说不出的情况下，你或许不希望这样报错，或许希望能够有某种别的提示、操作等。也就是我们更希望能在成员不存在的时候有所作为，不是等着报错。

要处理类似的问题，就要用到本节中的知识了。

##`__getattr__`、`__setattr__`和其它类似方法

还是用上面的例子，如果访问`a.x`，它不存在，那么就要转向到某个操作。我们把这种情况称之为“拦截”。就好像“寻隐者不遇”，却被童子“遥指杏花村”，将你“拦截”了。在Python中，有一些方法就具有这种“拦截”能力。

- `__setattr__(self,name,value)`：如果要给name赋值，就调用这个方法。
- `__getattr__(self,name)`：如果name被访问，同时它不存在的时候，此方法被调用。
- `__getattribute__(self,name)`：当name被访问时自动被调用（注意：这个仅能用于新式类），无论name是否存在，都要被调用。
- `__delattr__(self,name)`：如果要删除name，这个方法就被调用。

如果一时没有理解，不要紧，是正常的。需要用例子说明。

    >>> class A(object):
    ...     def __getattr__(self, name):
    ...         print "You use getattr"
    ...     def __setattr__(self, name, value):
    ...         print "You use setattr"
    ...         self.__dict__[name] = value
    ... 

类A是新式类，除了两个方法，没有别的属性。

    >>> a = A()
    >>> a.x
    You use getattr

`a.x`，按照本节开头的例子，是要报错的。但是，由于在这里使用了`__getattr__(self, name)`方法，当发现`x`不存在于对象的`__dict__`中的时候，就调用了`__getattr__`，即所谓“拦截成员”。
   
    >>> a.x = 7
    You use setattr

给对象的属性赋值时候，调用了`__setattr__(self, name, value)`方法，这个方法中有一句`self.__dict__[name] = value`，通过这个语句，就将属性和数据保存到了对象的`__dict__`中，如果在调用这个属性：

    >>> a.x
    7

它已经存在于对象的`__dict__`之中。

在上面的类中，当然可以使用`__getattribute__(self, name)`，因为它是新式类。并且，只要访问属性就会调用它。例如：

    >>> class B(object):
    ...     def __getattribute__(self, name):
    ...         print "you are useing getattribute"
    ...         return object.__getattribute__(self, name)
    ...

为了与前面的类区分，新命名一个类名字。需要提醒注意，在这里返回的内容用的是`return object.__getattribute__(self, name)`，而没有使用`return self.__dict__[name]`像是。因为如果用这样的方式，就是访问`self.__dict__`，只要访问这个属性，就要调用`__getattribute__``，这样就导致了无线递归下去（死循环）。要避免之。
    
    >>> b = B()
    >>> b.y
    you are useing getattribute
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 4, in __getattribute__
    AttributeError: 'B' object has no attribute 'y'
    >>> b.two
    you are useing getattribute
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 4, in __getattribute__
    AttributeError: 'B' object has no attribute 'two'

访问不存在的成员，可以看到，已经被`__getattribute__`拦截了，虽然最后还是要报错的。

    >>> b.y = 8
    >>> b.y
    you are useing getattribute
    8

当给其赋值后，意味着已经在`__dict__`里面了，再调用，依然被拦截，但是由于已经在`__dict__`内，会把结果返回。

当你看到这里，是不是觉得上面的方法有点魔力呢？不错。但是，它有什么具体应用呢？看下面的例子，能给你带来启发。

    #!/usr/bin/env python
    # coding=utf-8

    """
    study __getattr__ and __setattr__
    """

    class Rectangle(object):
        """
        the width and length of Rectangle
        """
        def __init__(self):
            self.width = 0
            self.length = 0

        def setSize(self, size):
            self.width, self.length = size
        def getSize(self):
            return self.width, self.length

    if __name__ == "__main__":
        r = Rectangle()
        r.width = 3
        r.length = 4
        print r.getSize()
        r.setSize( (30, 40) )
        print r.width
        print r.length

上面代码来自《Beginning Python:From Novice to Professional,Second Edittion》（by Magnus Lie Hetland），根据本教程的需要，稍作修改。

    $ python 21301.py 
    (3, 4)
    30
    40

这段代码已经可以正确运行了。但是，作为一个精益求精的程序员。总觉得那种调用方式还有可以改进的空间。比如，要给长宽赋值的时候，必须赋予一个元组，里面包含长和宽。这个能不能改进一下呢？

    #!/usr/bin/env python
    # coding=utf-8

    """
    study __getattr__ and __setattr__
    """

    class Rectangle(object):
        """
        the width and length of Rectangle
        """
        def __init__(self):
            self.width = 0
            self.length = 0

        def setSize(self, size):
            self.width, self.length = size
        def getSize(self):
            return self.width, self.length
        
        size = property(getSize, setSize)

    if __name__ == "__main__":
        r = Rectangle()
        r.width = 3
        r.length = 4
        print r.size
        r.size = 30, 40
        print r.width
        print r.length

以上代码的运行结果同上。但是，因为加了一句`size = property(getSize, setSize)`，使得调用方法是不是更优雅了呢？原来用`r.getSize()`，现在使用`r.size`，就好像调用一个属性一样。难道你不觉得眼熟吗？在[《多态和封装》](./211.md)中已经用到过property函数了，虽然写法略有差别，但是作用一样。

本来，这样就已经足够了。但是，因为本节中出来了特殊方法，所以，一定要用这些特殊方法从新演绎一下这段程序。虽然重新演绎的不一定比原来的好，主要目的是演示本节的特殊方法应用。

    #!/usr/bin/env python
    # coding=utf-8

    class NewRectangle(object):
        def __init__(self):
            self.width = 0
            self.length = 0

        def __setattr__(self, name, value):
            if name == "size":
                self.width, self.length = value
            else:
                self.__dict__[name] = value

        def __getattr__(self, name):
            if name == "size":
                return self.width, self.length
            else:
                raise AttributeError

    if __name__ == "__main__":
        r = NewRectangle()
        r.width = 3
        r.length = 4
        print r.size
        r.size = 30, 40
        print r.width
        print r.length

除了类的样式变化之外，调用样式没有变。结果是一样的。

这就算了解了一些这些属性了吧。但是，有一篇文章是要必须推荐给读者阅读的：[Python Attributes and Methods](http://www.cafepy.com/article/python_attributes_and_methods/python_attributes_and_methods.html)，读了这篇文章，对python的对象属性和方法会有更深入的理解。

##获得属性顺序

通过实例获取其属性（也有说特性的，名词变化了，但是本质都是属性和方法），如果在`__dict__`中有相应的属性，就直接返回其结果；如果没有，会到类属性中找。比如：

    #!/usr/bin/env python
    # coding=utf-8

    class A(object):
        author = "qiwsir"
        def __getattr__(self, name):
            if name != "author":
                return "from starter to master."

    if __name__ == "__main__":
        a = A()
        print a.author
        print a.lang

运行程序：

    $ python 21302.py 
    qiwsir
    from starter to master.

当`a = A()`后，并没有为实例建立任何属性，或者说实例的`__dict__`是空的，这在上节中已经探讨过了。但是如果要查看`a.author`，因为实例的属性中没有，所以就去类属性中找，发现果然有，于是返回其值`"qiwsir"`。但是，在找`a.lang`的时候，不仅实例属性中没有，类属性中也没有，于是就调用了`__getattr__()`方法。在上面的类中，有这个方法，如果没有`__getattr__()`方法呢？如果没有定义这个方法，就会引发AttributeError，这在前面已经看到了。

这就是通过实例查找特性的顺序。

##双下划线

至此，是否注意到，我们使用很多以双下划线开头和结尾的方法名，比如`__dict__`，`__init__`个。在Python中，用这种方法表示特殊的方法名，当然，这是一个惯例，之所以这样做，主要是确保这些特殊的方法名不会跟你自己所定义的名称冲突，我们自己定义名称的时候，是绝少用双划线开头和结尾的。如果你需要重写这些方法，当然是可以的，具体参看前文关于继承的讲述。

------
