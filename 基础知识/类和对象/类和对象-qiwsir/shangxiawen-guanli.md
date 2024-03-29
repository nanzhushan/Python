>要使人晓得智慧和训诲，分辨通达的言语。使人处事，领受智慧、仁义、公平、正直的训诲。使愚人灵明、使少年人有知识和谋略。使智慧人听见、增长学问、使聪明人得着智谋、使人明白箴言和譬喻、懂得智慧人的言词和谜语。敬畏耶和华使知识的开端，愚妄人藐视智慧和训诲。

#上下文管理器

在[《文件(1)》](./126.md)中提到，如果要打开文件，一种比较好的方法是使用`with`语句，因为这种方法，不仅结构简单，更重要的是不用再单独去判断某种异常情况，也不用专门去执行文件关闭的指令了。

本节对这个有点神奇的`with`进行深入剖析。

##概念

跟`with`相关的有一些概念，需要必须澄清。

**上下文管理**

如果把它作为一个概念来阐述，似乎有点多余，因为从字面上也可以有一丝的体会，但是，我要说的是，那点直觉的体会不一定等于理性的严格定义，特别是周遭事物越来越复杂的时候。

“上下文”的英文是context，在网上检索了一下关于“上下文”的说法，发现没有什么严格的定义，另外，不同的语言环境，对“上下文管理”有不同的说法。根据我个人的经验和能看到的某些资料，我以为可以把“上下文”理解为某一些语句构成的一个环境（也可以说是代码块），所谓“管理”就是要在这个环境中做一些事情，做什么事情呢？就Python而言，是要将前面某个语句（“上文”）干的事情独立成为对象，然后在后面（“下文”）中使用这个对象来做事情。

**上下文管理协议**

英文是Context Management Protocol，既然是协议，就应该是包含某些方法的东西，大家都按照这个去做（协商好了的东西）。Python中的上下文管理协议中必须包含`__enter__()`和`__exit__()`两个方法。

看这个两个方法的名字，估计读者也能领悟一二了（名字不是随便取的，这个某个岛国取名字的方法不同，当然，现在人家也不是随便取了）。

**上下文管理器**

网上能够找到的最通常的说法是：上下文管理器是支持上下文管理协议的对象，这种对象实现了`__enter__()`和`__exit__()`方法。

这个简洁而准确的定义，一般情况下一些高手是理解了。如果读者有疑惑，就说明...，我还是要把一个高雅的定义通俗化更好一些。

在Python中，下面的语句，也存在上下文，但它们是一气呵成执行的。

    >>> name = "laoqi"
    >>> if name == "laoqi":
    ...     print name
    ... 
    laoqi
    >>> if name == "laoqi":
    ...     for i in name:
    ...         print i,
    ... 
    l a o q i

以上两个例子中，“上文”进行了判断，然后“下文”执行，从上而下，已经很通畅了。还有不那么通畅的，就是下面的情况。

    >>> f = open("a.txt", "w")
    >>> f.write("hello")
    >>> f.write("python")
    >>> f.close()

在这个示例中，当`f = open("a.txt", "w")`之后，其实这句话并没有如同前面的示例中那样被“遗忘”，它是让计算机运行到一种状态——文件始终处于打开状态——然后在这种状态中进行后面的操作，直到`f.close()`为止，这种状态才结束。

在这种情况下，我们就可以使用“上下文管理器”（英文：Context Manager），用它来获得“上文”状态对象，然后在“下文”使用它，并在整个过程执行完毕来收场。

更Python一点的说法，可以说是在某任务执行之初，上下文管理器做好执行准备，当任务（代码块）执行完毕或者中间出现了异常，上下文管理器负责结束工作。

这么好的一个东西，是Python2.5以后才进来的。

##必要性

刚才那个向文件中写入hello和python两个单词的示例，如果你觉得在工程中也可以这样做，就大错特错了。因为它存在隐含的问题，比如在写入了hello之后，不知道什么原因，后面的python不能写入了，最能说服你的是恰好遇到了“磁盘已满”——虽然这种情况的概率可能比抓奖券还小，但作为严谨的程序员，是必须要考虑的，这也是程序复杂之原因，这时候后面的操作就出现了异常，无法执行，文件也不能close。解决这个问题的方法是用`try ... finally ...`语句，读者一定能写出来。

不错，的确解决了。

问题继续，如果要从一个文件读内容，写入到另外一个文件中，下面的样子你觉得如何？

首先建立一个文件，名称为23501.txt，里面的内容如下：

    $ cat 23501.txt
    hello laoqi
    www.itdiffer.com

然后写出下面的代码，实现上述目的：


    #!/usr/bin/env python
    # coding=utf-8

    read_file = open("23501.txt")
    write_file = open("23502.txt", "w")

    try:
        r = read_file.readlines()
        for line in r:
            write_file.write(line)
    finally:
        read_file.close()
        write_file.close()

如果你不知道“上下文管理器”，这样做无可厚非，可偏偏现在已经知道了，所以，从今以后这样做就不是最优的了，因为它可以用“上下文管理器”写的更好。所以，用`with`语句改写之后，就是很优雅的了。

    with open("23501.txt") as read_file, open("23503.txt", "w") as write_file:
        for line in read_file.readlines():
            write_file.write(line)

跟前面的对比一下，是不是有点惊叹了？！所以，你可以理直气壮地说“我用Python”。

可见上下文管理器是必要的，因为它让代码优雅了，当然优雅只是表象，还有更深层次的含义，继续阅读下面的内容能有深入体会。

**更深入**

前面已经说了，上下文管理器执行了`__enter__()`和`__exit__()`方法，可是在`with`语句中哪里看到了这两个方法呢？

为了解把这个问题解释清楚，需要先做点别的操作，虽然工程中一般不需要做。


    #!/usr/bin/env python
    # coding=utf-8

    class ContextManagerOpenDemo(object):

        def __enter__(self):
            print "Starting the Manager."

        def __exit__(self, *others):
            print "Exiting the Manager."

    with ContextManagerOpenDemo():
        print "In the Manager."

在上面的代码示例中，我们写了一个类`ContextManagerOpenDemo()`，你就把它理解为我自己写的`Open()`吧，当然使最简版本了。在这个类中，`__enter__()`方法和`__exit__()`方法都比较简单，就是要检测是否执行该方法。

然后用`with`语句来执行，目的是按照“上下文管理器”的解释那样，应该首先执行类中的`__enter__()`方法，它总是在进入代码块前被调用的，接着就执行代码块——`with`语句下面的内容，当代码块执行完毕，离开的时候又调用类中的`__exit__()`。

检验一下，是否按照上述理想路径执行。

    $ python 23502.py
    Starting the Manager.
    In the Manager.
    Exiting the Manager.

果然如此。执行结果已经基本显示了上下文管理器的工作原理。

为了让它更接近`open()`，需要再进一步改写，让它能够接受参数，以便于指定打开的文件。

    #!/usr/bin/env python
    # coding=utf-8

    class ContextManagerOpenDemo(object):
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode

        def __enter__(self):
            print "Starting the Manager."
            self.open_file = open(self.filename, self.mode)
            return self.open_file

        def __exit__(self, *others):
            self.open_file.close()
            print "Exiting the Manager."

    with ContextManagerOpenDemo("23501.txt", 'r') as reader:
        print "In the Manager."
        for line in reader:
            print line

这段代码的意图主要是：

1. 通过`__init__()`能够读入文件名和打开模式，以使得看起来更接近`open()`；
2. 当进入语句块时，先执行`__enter__()`方法，把文件打开，并返回该文件对象；
3. 执行代码块内容，打印文件内容；
4. 离开代码块的时候，执行`__exit__()`方法，关闭文件。

运行结果是：

    $ python 23502.py
    Starting the Manager.
    In the Manager.
    hello laoqi

    www.itdiffer.com

    Exiting the Manager.

在上述代码中，我们没有对异常进行处理，也就是把异常隐藏了，不管在代码块执行时候遇到什么异常，都是要离开代码块，那么就立刻让`__exit__()`方法接管了。

如果要把异常显现出来，也使可以，可以改写`__exit__()`方法。例如：

    def __exit__(self, exc_type, exc_value, exc_traceback):
        return False

当代码块出现异常，则由`__exit__()`负责善后清理，如果返回False，如上面的示例，则异常让`with`之外的语句逻辑来处理，这是通常使用的方法；如果返回True，意味着不对异常进行处理。

从上面我们自己写的类和方法中，已经了解了上下文管理器的运行原理了。那么，`open()`跟它有什么关系吗？

为了能清楚地查看，我们需要建立一个文件对象，并且使用`dir()`来看看是否有我们所期盼的东西。

    >>> f = open("a.txt")
    >>> dir(f)
        ['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'closed', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'mode', 'name', 'newlines', 'next', 'read', 'readinto', 'readline', 'readlines', 'seek', 'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines']

读者是否运用你那迷迷糊糊的火眼金睛看到了两个已经很面熟的方法名称了？如果你找到了，你就心知肚明了。

在`with`语句中还有一个`as`，虽然在上面示例中没有显示，但是一般我们还是不抛弃它的，它的作用就是将返回的对象付给一个变量，以便于以后使用。

##contextlib模块

Python中的这个模块使上下文管理中非常好用的东东，这也是标准库中的一员，不需要另外安装了。

    >>> import contextlib
    >>> dir(contextlib)
        ['GeneratorContextManager', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'closing', 'contextmanager', 'nested', 'sys', 'warn', 'wraps']

常用的是`contextmanger`、`closing`和`nested`。

###contextlib.closing()

要想知道`contextlib.closing()`的使用方法，最常用的方法就是`help()`，这是我们的一贯做法，胜过查阅其它任何资料。

    Help on class closing in module contextlib:

    class closing(__builtin__.object)
    |  Context to automatically close something at the end of a block.
    |  
    |  Code like this:
    |  
    |      with closing(<module>.open(<arguments>)) as f:
    |          <block>
    |  

以上省略了部分内容。

有一种或许常用到的情景，就是连接数据库，并返回一个数据库对象，在使用完之后关闭数据库连接，其形状如下：

    with contextlib.closing(CreateDB()) as db:
        db.query()

以上不是可运行的代码，只是一个架势，读者如果在编码中使用，需要根据实际情况改写。

当数据库语句`db.query()`结束之后，数据库连接自动关闭。

###contextlib.nested()

nested的汉语意思是“嵌套的，内装的”，从字面上读者也可能理解了，这个方法跟嵌套有关。前面有一个示例，是从一个文件读取，然后写入到另外一个文件。我不知道读者是否想过可以这么写：

    with open("23501.txt") as read_file：
        with open("23503.txt", "w") as write_file:
            for line in read_file.readlines():
                write_file.write(line)

此种写法不是不行，但是不提倡，因为它太不Pythoner了。其实这里就涉及到了嵌套，因此可以使用`contextlib.nested`重写。

    with contextlib.nested(open("23501.txt", "r"), open("23503.txt", "w")) as (read_file, write_file):
        for line in read_file.readlines():
            write_file.write(line)

这是一种不错的写法，当然，在本节最前面所用到的写法，也是可以的，只要不用刚才那种嵌套。

###contextlib.contextmanager

contextlib.contextmanager是一个装饰器，它作用于生成器函数（也就是带有yield的函数），一单生成器函数被装饰以后，就返回一个上下文管理器，即contextlib.contextmanager因为装饰了一个生成器函数而产生了`__enter__()`和`__exit__()`方法。例如：

特别要提醒，被装饰的生成器函数只能产生一个值，否则就会抛出RuntimeError异常；如果有as子句，则所产生的值，会通过as子句赋给某个变量，就如同前面那样，例如下面的示例（本示例来自：http://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/index.html）。

    #!/usr/bin/env python
    # coding=utf-8

    from contextlib import contextmanager

    @contextmanager
    def demo():
        print "before yield."
        yield "contextmanager demo."
        print "after yield."

    with demo() as dd:
        print "the word is: %s" % dd

运行结果是：

    $ python 23504.py
    before yield.
    the word is: contextmanager demo.
    after yield.

为了好玩，再借用网上的一个示例，理解这个装饰器的作用（下面代码来自：http://preshing.com/20110920/the-python-with-statement-by-example/），代码中用到了`cairo`模块，该模块的安装方法是：

    sudo apt-get install libcairo2-dev
	
如果是windows操作系统，可以到官方网站下载：[http://cairographics.org/](http://cairographics.org/)

所执行的代码如下：

    #!/usr/bin/env python
    # coding=utf-8

    import cairo
    from contextlib import contextmanager

    @contextmanager
    def saved(cr):
        cr.save()
        try:
            yield cr
        finally:
            cr.restore()

    def tree(angle):
        cr.move_to(0, 0)
        cr.translate(0, -65)
        cr.line_to(0, 0)
        cr.stroke()
        cr.scale(0.72, 0.72)
        if angle > 0.72:
            for a in [-angle, angle]:
                with saved(cr):
                    cr.rotate(a)
                    tree(angle * 0.75)

    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, 280, 204)
    cr = cairo.Context(surf)
    cr.translate(140, 203)
    cr.set_line_width(5)
    tree(0.75)
    surf.write_to_png('fractal-tree.png')

不过，我感到很奇怪，我得到的图片是这样的：

![](./2code/fractal-tree.png)

而原文中得到的图片是这样的：

![](http://preshing.com/images/tree.png)

请读者指正。

--------
