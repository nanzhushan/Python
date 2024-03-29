>你竟任着刚硬不悔改的心，为自己积蓄忿怒，以致神震怒，显他公义审判的日子来到。他必照各人的行为报应各人。凡恒心行善，寻求荣耀、尊贵和不能朽坏之福的，就以永生报应他们；惟有结党不顺从真理，反顺从不义的，就以忿怒、恼恨报应他们。(ROMANS 2:7-8)

#迭代

跟一些比较牛X的程序员交流，经常听到他们嘴里冒出一个不标准的英文单词，而loop、iterate、traversal和recursion如果不在其内，总觉得他还不够牛X。当让，真正牛X的绝对不会这么说的，他们只是说“循环、迭代、遍历、递归”，然后再问“这个你懂吗？”。哦，这就是真正牛X的程序员。不过，他也仅仅是牛X罢了，还不是大神。大神程序员是什么样儿呢？他是扫地僧，大隐隐于市。

先搞清楚这些名词再说别的：

- 循环（loop），指的是在满足条件的情况下，重复执行同一段代码。比如，while语句。
- 迭代（iterate），指的是按照某种顺序逐个访问列表中的每一项。比如，for语句。
- 递归（recursion），指的是一个函数不断调用自身的行为。比如，以编程方式输出著名的斐波纳契数列。
- 遍历（traversal），指的是按照一定的规则访问树形结构中的每个节点，而且每个节点都只访问一次。

对于这四个听起来高深莫测的词汇，其实前面，已经涉及到了一个——循环（loop），本节主要介绍一下迭代（iterate），看官在网上google，就会发现，对于迭代和循环、递归之间的比较的文章不少，分别从不同角度将它们进行了对比。这里暂不比较，先搞明白python中的迭代。

当然，迭代的话题如果要说起来，会很长，本着循序渐进的原则，这里介绍比较初级的。

##逐个访问

在python中，访问对象中每个元素，可以这么做：（例如一个list）

    >>> lst
    ['q', 'i', 'w', 's', 'i', 'r']
    >>> for i in lst:
    ...     print i,
    ... 
    q i w s i r

除了这种方法，还可以这样：

    >>> lst_iter = iter(lst)    #对原来的list实施了一个iter()
    >>> lst_iter.next()         #要不厌其烦地一个一个手动访问
    'q'
    >>> lst_iter.next()
    'i'
    >>> lst_iter.next()
    'w'
    >>> lst_iter.next()
    's'
    >>> lst_iter.next()
    'i'
    >>> lst_iter.next()
    'r'
    >>> lst_iter.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

> 在python3中, lst_iter.next()方法变成了lst_iter.\_\_next__(). 取而代之的是next(lst_iter).

`iter()`是一个内建函数，其含义是：

上面的`next()`就是要获得下一个元素，但是做为一名优秀的程序员，最佳品质就是“懒惰”，当然不能这样一个一个地敲啦，于是就：

    >>> while True:
    ...     print lst_iter.next()
    ... 
    Traceback (most recent call last):      #居然报错，而且错误跟前面一样？什么原因
      File "<stdin>", line 2, in <module>
    StopIteration

先不管错误，再来一遍。
    
    >>> lst_iter = iter(lst)                #上面的错误暂且搁置，回头在研究
    >>> while True:
    ...     print lst_iter.next()
    ... 
    q                                       #果然自动化地读取了
    i
    w
    s
    i
    r
    Traceback (most recent call last):      #读取到最后一个之后，报错，停止循环
      File "<stdin>", line 2, in <module>
    StopIteration

首先了解一下上面用到的那个内置函数：iter(),官方文档中有这样一段话描述之：

> iter(o[, sentinel])

>  Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument. Without a second argument, o must be a collection object which supports the iteration protocol (the __iter__() method), or it must support the sequence protocol (the __getitem__() method with integer arguments starting at 0). If it does not support either of those protocols, TypeError is raised. If the second argument, sentinel, is given, then o must be a callable object. The iterator created in this case will call o with no arguments for each call to its next() method; if the value returned is equal to sentinel, StopIteration will be raised, otherwise the value will be returned.

大意是说...(此处故意省略若干字，因为我相信看此文章的看官英语水平是达到看文档的水平了，如果没有，也不用着急，找个词典什么的帮助一下。)

尽管不翻译了，但是还要提炼一下主要的东西：

- 返回值是一个迭代器对象
- 参数需要是一个符合迭代协议的对象或者是一个序列对象
- next()配合与之使用

什么是“可迭代的对象”呢？在前面学习的时候，曾经提到过，如果忘记了请往前翻阅。

一般，我们常常将哪些能够用诸如循环语句之类的方法来一个一个读取元素的对象，就称之为可迭代的对象。那么用来循环的如for就被称之为迭代工具。

用严格点的语言说：所谓迭代工具，就是能够按照一定顺序扫描迭代对象的每个元素（按照从左到右的顺序）。

显然，除了for之外，还有别的可以称作迭代工具。

那么，刚才介绍的iter()的功能呢？它与next()配合使用，也是实现上述迭代工具的作用。

在python中，甚至在其它的语言中，迭代这块的说法比较乱，主要是名词乱，刚才我们说，那些能够实现迭代的东西，称之为迭代工具，就是这些迭代工具，不少程序员都喜欢叫做迭代器。当然，这都是汉语翻译，英语就是iterator。

看官看上面的所有例子会发现，如果用for来迭代，当到末尾的时候，就自动结束了，不会报错。如果用iter()...next()迭代，当最后一个完成之后，它不会自动结束，还要向下继续，但是后面没有元素了，于是就报一个称之为StopIteration的错误（这个错误的名字叫做：停止迭代，这哪里是报错，分明是警告）。

看官还要关注iter()...next()迭代的一个特点。当迭代对象lst_iter被迭代结束，即每个元素都读取了一遍之后，指针就移动到了最后一个元素的后面。如果再访问，指针并没有自动返回到首位置，而是仍然停留在末位置，所以报StopIteration，想要再开始，需要重新载入迭代对象。所以，当我在上面重新进行迭代对象赋值之后，又可以继续了。这在for等类型的迭代工具中是没有的。

##文件迭代器

现在有一个文件，名称：208.txt，其内容如下：

    Learn python with qiwsir.
    There is free python course.
    The website is:
    http://qiwsir.github.io
    Its language is Chinese.

用迭代器来操作这个文件，我们在前面讲述文件有关知识的时候已经做过了，无非就是：

    >>> f = open("208.txt")
    >>> f.readline()        #读第一行
    'Learn python with qiwsir.\n'
    >>> f.readline()        #读第二行
    'There is free python course.\n'
    >>> f.readline()        #读第三行
    'The website is:\n'
    >>> f.readline()        #读第四行
    'http://qiwsir.github.io\n'
    >>> f.readline()        #读第五行，也就是这真在读完最后一行之后，到了此行的后面
    'Its language is Chinese.\n'
    >>> f.readline()        #无内容了，但是不报错，返回空。
    ''

以上演示的是用readline()一行一行地读。当然，在实际操作中，我们是绝对不能这样做的，一定要让它自动进行，比较常用的方法是：

    >>> for line in f:     #这个操作是紧接着上面的操作进行的，请看官主要观察
    ...     print line,    #没有打印出任何东西 
    ... 

这段代码之所没有打印出东西来，是因为经过前面的迭代，指针已经移到了最后了。这就是迭代的一个特点，要小心指针的位置。

    >>> f = open("208.txt")     #从头再来
    >>> for line in f:
    ...     print line,
    ... 
    Learn python with qiwsir.
    There is free python course.
    The website is:
    http://qiwsir.github.io
    Its language is Chinese.

这种方法是读取文件常用的。另外一个readlines()也可以。但是，需要有一些小心的地方，看官如果想不起来小心什么，可以再将关于文件的课程复习一遍。

上面过程用next()也能够读取。

    >>> f = open("208.txt")
    >>> f.next()
    'Learn python with qiwsir.\n'
    >>> f.next()
    'There is free python course.\n'
    >>> f.next()
    'The website is:\n'
    >>> f.next()
    'http://qiwsir.github.io\n'
    >>> f.next()
    'Its language is Chinese.\n'
    >>> f.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

如果用next()，就可以直接读取每行的内容。这说明文件是天然的可迭代对象，不需要用iter()转换了。

再有，我们用for来实现迭代，在本质上，就是自动调用next()，只不过这个工作，已经让for偷偷地替我们干了，到这里，列位是不是应该给for取另外一个名字：它叫雷锋。

还有，列表解析也能够做为迭代工具，在研究列表的时候，看官想必已经清楚了。那么对文件，是否可以用？试一试：

    >>> [ line for line in open('208.txt') ]
    ['Learn python with qiwsir.\n', 'There is free python course.\n', 'The website is:\n', 'http://qiwsir.github.io\n', 'Its language is Chinese.\n']

至此，看官难道还不为列表解析所折服吗？真的很强大，又强又大呀。

其实，迭代器远远不止上述这么简单，下面我们随便列举一些，在python中还可以这样得到迭代对象中的元素。

    >>> list(open('208.txt'))
    ['Learn python with qiwsir.\n', 'There is free python course.\n', 'The website is:\n', 'http://qiwsir.github.io\n', 'Its language is Chinese.\n']
    
    >>> tuple(open('208.txt'))
    ('Learn python with qiwsir.\n', 'There is free python course.\n', 'The website is:\n', 'http://qiwsir.github.io\n', 'Its language is Chinese.\n')
    
    >>> "$$$".join(open('208.txt'))
    'Learn python with qiwsir.\n$$$There is free python course.\n$$$The website is:\n$$$http://qiwsir.github.io\n$$$Its language is Chinese.\n'
    
    >>> a,b,c,d,e = open("208.txt")
    >>> a
    'Learn python with qiwsir.\n'
    >>> b
    'There is free python course.\n'
    >>> c
    'The website is:\n'
    >>> d
    'http://qiwsir.github.io\n'
    >>> e
    'Its language is Chinese.\n'

上述方式，在编程实践中不一定用得上，只是向看官展示一下，并且看官要明白，可以这么做，不是非要这么做。

补充一下，字典也可以迭代，看官自己不妨摸索一下（其实前面已经用for迭代过了，这次请摸索一下用iter()...next()手动一步一步迭代）。

------
