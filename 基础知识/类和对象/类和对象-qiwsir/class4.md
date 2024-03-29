>你们仍是属肉体的，因为在你们中间有嫉妒分争，这岂不是属乎肉体，照着世人的样子行吗？...我栽种了，亚波罗浇灌了，惟有神叫他生长。(1 CORINTHIANS 3:3,6)

#类(4)

本节介绍类中一个非常重要的东西——继承，其实也没有那么重要，只是听起来似乎有点让初学者晕头转向，然后就感觉它属于很高级的东西，真是情况如何？学了之后你自然有感受。

在现实生活中，“继承”意味着一个人从另外一个人那里得到了一些什么，比如“继承革命先烈的光荣传统”、“某人继承他老爹的万贯家产”等。总之，“继承”之后，自己就在所继承的方面省力气、不用劳神费心，能轻松得到，比如继承了万贯家产，自己就一夜之间变成富豪。如果继承了“革命先烈的光荣传统”，自己是不是一下就变成革命者呢？

当然，生活中的继承或许不那么严格，但是编程语言中的继承是有明确规定和稳定的预期结果的。

>继承（Inheritance）是面向对象软 件技术当中的一个概念。如果一个类别A“继承自”另一个类别B，就把这个A称为“B的子类别”，而把B称为“A的父类别”，也可以称“B是A的超类”。

>继承可以使得子类别具有父类别的各种属性和方法，而不需要再次编写相同的代码。在令子类别继承父类别的同时，可以重新定义某些属性，并重写某些方法，即覆盖父类别的原有属性和方法，使其获得与父类别不同的功能。另外，为子类别追加新的属性和方法也是常见的做法。 （源自维基百科）

由上面对继承的表述，可以简单总结出继承的意图或者好处：

- 可以实现代码重用，但不是仅仅实现代码重用，有时候根本就没有重用
- 实现属性和方法继承

诚然，以上也不是全部，随着后续学习，对继承的认识会更深刻。好友令狐虫曾经这样总结继承：

>从技术上说，OOP里，继承最主要的用途是实现多态。对于多态而言，重要的是接口继承性，属性和行为是否存在继承性，这是不一定的。事实上，大量工程实践表明，重度的行为继承会导致系统过度复杂和臃肿，反而会降低灵活性。因此现在比较提倡的是基于接口的轻度继承理念。这种模型里因为父类（接口类）完全没有代码，因此根本谈不上什么代码复用了。

>在Python里，因为存在Duck Type，接口定义的重要性大大的降低，继承的作用也进一步的被削弱了。

>另外，从逻辑上说，继承的目的也不是为了复用代码，而是为了理顺关系。

他是大牛，或许读者感觉比较高深，没关系，随着你的实践经验的积累，你也能对这个问题有自己独到的见解。

或许你也要问我的观点是什么？我的观点就是：走着瞧！怎么理解？继续向下看，只有你先深入这个问题，才能跳到更高层看这个问题。小马过河的故事还记得吧？只有亲自走入河水中，才知道河水的深浅。

对于python中的继承，前面一直在使用，那就是我们写的类都是新式类，所有新式类都是继承自object类。不要忘记，新式类的一种写法：

    class NewStyle(object):
        pass
        
这就是典型的继承。

##基本概念

    #!/usr/bin/env python
    # coding=utf-8

    __metaclass__ = type

    class Person:
        def speak(self):
            print "I love you."

        def setHeight(self):
            print "The height is: 1.60m ."

        def breast(self, n):
            print "My breast is: ",n

    class Girl(Person):
        def setHeight(self):
            print "The height is:1.70m ."

    if __name__ == "__main__":
        cang = Girl()
        cang.setHeight()
        cang.speak()
        cang.breast(90)

上面这个程序，保存之后运行：

    $ python 20901.py 
    The height is:1.70m .
    I love you.
    My breast is:  90

对以上程序进行解释，从中体会继承的概念和方法。

首先定义了一个类Person，在这个类中定义了三个方法。注意，没有定义初始化函数，初始化函数在类中不是必不可少的。

然后又定义了一个类Girl，这个类的名字后面的括号中，是上一个类的名字，这就意味着Girl继承了Person，Girl是Person的子类，Person是Girl的父类。

既然是继承了Person，那么Girl就全部拥有了Person中的方法和属性（上面的例子虽然没有列出属性）。但是，如果Girl里面有一个和Person同样名称的方法，那么就把Person中的同一个方法遮盖住了，显示的是Girl中的方法，这叫做方法的**重写**。

实例化类Girl之后，执行实例方法`cang.setHeight()`，由于在类Girl中重写了setHeight方法，那么Person中的那个方法就不显作用了，在这个实例方法中执行的是类Girl中的方法。

虽然在类Girl中没有看到speak方法，但是因为它继承了Person，所以`cang.speak()`就执行类Person中的方法。同理`cang.breast(90)`，它们就好像是在类Girl里面已经写了这两个方法一样。既然继承了，就是我的了。

##多重继承

所谓多重继承，就是指某一个类的父类，不止一个，而是多个。比如：

    #!/usr/bin/env python
    # coding=utf-8

    __metaclass__ = type

    class Person:
        def eye(self):
            print "two eyes"

        def breast(self, n):
            print "The breast is: ",n

    class Girl:
        age = 28
        def color(self):
            print "The girl is white"

    class HotGirl(Person, Girl):
        pass

    if __name__ == "__main__":
        kong = HotGirl()
        kong.eye()
        kong.breast(90)
        kong.color()
        print kong.age

在这个程序中，前面有两个类：Person和Girl，然后第三个类HotGirl继承了这两个类，注意观察继承方法，就是在类的名字后面的括号中把所继承的两个类的名字写上。但是第三个类中什么方法也没有。

然后实例化类HotGirl，既然继承了上面的两个类，那么那两个类的方法就都能够拿过来使用。保存程序，运行一下看看

    $ python 20902.py 
    two eyes
    The breast is:  90
    The girl is white
    28
    
值得注意的是，这次在类Girl中，有一个`age = 28`，在对HotGirl实例化之后，因为继承的原因，这个类属性也被继承到HotGirl中，因此通过实例属性`kong.age`一样能够得到该数据。

由上述两个实例，已经清楚看到了继承的特点，即将父类的方法和属性全部承接到子类中；如果子类重写了父类的方法，就使用子类的该方法，父类的被遮盖。

##多重继承的顺序

多重继承的顺序很必要了解。比如，如果一个子类继承了两个父类，并且两个父类有同样的方法或者属性，那么在实例化子类后，调用那个方法或属性，是属于哪个父类的呢？造一个没有实际意义，纯粹为了解决这个问题的程序：

    #!/usr/bin/env python
    # coding=utf-8

    class K1(object):
        def foo(self):
            print "K1-foo"

    class K2(object):
        def foo(self):
            print "K2-foo"
        def bar(self):
            print "K2-bar"

    class J1(K1, K2):
        pass

    class J2(K1, K2):
        def bar(self):
            print "J2-bar"

    class C(J1, J2):
        pass

    if __name__ == "__main__":
        print C.__mro__
        m = C()
        m.foo()
        m.bar()

这段代码，保存后运行：

    $ python 20904.py 
    (<class '__main__.C'>, <class '__main__.J1'>, <class '__main__.J2'>, <class '__main__.K1'>, <class '__main__.K2'>, <type 'object'>)
    K1-foo
    J2-bar

代码中的`print C.__mro__`是要打印出类的继承顺序。从上面清晰看出来了。如果要执行foo()方法，首先看J1，没有，看J2，还没有，看J1里面的K1，有了，即C==>J1==>J2==>K1；bar()也是按照这个顺序，在J2中就找到了一个。

这种对继承属性和方法搜索的顺序称之为“广度优先”。

新式类用以及python3.x中都是按照此顺序原则搜寻属性和方法的。

但是，在旧式类中，是按照“深度优先”的顺序的。因为后面读者也基本不用旧式类，所以不举例。如果读者愿意，可以自己模仿上面代码，探索旧式类的“深度优先”含义。

##super函数

对于初始化函数的继承，跟一般方法的继承，还有点不同。可以看下面的例子：

    #!/usr/bin/env python
    # coding=utf-8

    __metaclass__ = type

    class Person:
        def __init__(self):
            self.height = 160

        def about(self, name):
            print "{} is about {}".format(name, self.height)

    class Girl(Person):
        def __init__(self):
            self.breast = 90

        def about(self, name):
            print "{} is a hot girl, she is about {}, and her breast is {}".format(name, self.height, self.breast)

    if __name__ == "__main__":
        cang = Girl()
        cang.about("canglaoshi")

在上面这段程序中，类Girl继承了类Person。在类Girl中，初始化设置了`self.breast = 90`，由于继承了Person，按照前面的经验，Person的初始化函数中的`self.height = 160`也应该被Girl所继承过来。然后在重写的about方法中，就是用`self.height`。

实例化类Girl，并执行`cang.about("canglaoshi")`，试图打印出一句话`canglaoshi is a hot girl, she is about 160, and her bereast is 90`。保存程序，运行之：

    $ python 20903.py 
    Traceback (most recent call last):
      File "20903.py", line 22, in <module>
        cang.about("canglaoshi")
      File "20903.py", line 18, in about
        print "{} is a hot girl, she is about {}, and her breast is {}".format(name, self.height, self.breast)
    AttributeError: 'Girl' object has no attribute 'height'

报错！

程序员有一句名言：不求最好，但求报错。报错不是坏事，是我们长经验的时候，是在告诉我们，那么做不对。

重要的是看报错信息。就是我们要打印的那句话出问题了，报错信息显示`self.height`是不存在的。也就是说类Girl没有从Person中继承过来这个属性。

原因是什么？仔细观察类Girl，会发现，除了刚才强调的about方法重写了,`__init__`方法，也被重写了。不要认为它的名字模样奇怪，就不把它看做类中的方法（函数），它跟类Person中的`__init__`重名了，也同样是重写了那个初始化函数。

这就提出了一个问题。因为在子类中重写了某个方法之后，父类中同样的方法被遮盖了。那么如何再把父类的该方法调出来使用呢？纵然被遮盖了，应该还是存在的，不要浪费了呀。

python中有这样一种方法，这种方式是被提倡的方法：super函数。

    #!/usr/bin/env python
    # coding=utf-8

    __metaclass__ = type

    class Person:
        def __init__(self):
            self.height = 160

        def about(self, name):
            print "{} is about {}".format(name, self.height)

    class Girl(Person):
        def __init__(self):
            super(Girl, self).__init__()
            self.breast = 90

        def about(self, name):
            print "{} is a hot girl, she is about {}, and her breast is {}".format(name, self.height, self.breast)
            super(Girl, self).about(name)

    if __name__ == "__main__":
        cang = Girl()
        cang.about("canglaoshi")

在子类中，`__init__`方法重写了，为了调用父类同方法，使用`super(Girl, self).__init__()`的方式。super函数的参数，第一个是当前子类的类名字，第二个是self，然后是点号，点号后面是所要调用的父类的方法。同样在子类重写的about方法中，也可以调用父类的about方法。

执行结果：

    $ python 20903.py 
    canglaoshi is a hot girl, she is about 160, and her breast is 90
    canglaoshi is about 160

最后要提醒注意：super函数仅仅适用于新式类。当然，你一定是使用的新式类。“喜新厌旧”是程序员的嗜好。

------
