>弟兄们，那些离间你们，叫你们跌倒，背乎所学之道的人，我劝你们要留意躲避他们。因为这样的人不服侍我们的主基督，只服侍自己的肚腹，用花言巧语诱惑那些老实人的心。(ROMANS 16:17-18)

#类(2)

现在开始不用伪代码了，用真正的python代码来理解类。当然，例子还是要用读者感兴趣的例子。

##新式类和旧式类

因为python是一个不断发展的高级语言（似乎别的语言是不断发展的，甚至于自然语言也是），导致了在python2.x的版本中，有“新式类”和“旧式类（也叫做经典类）”之分。新式类是python2.2引进的，在此后的版本中，我们一般用的都是新式类。本着知其然还要知其所以然的目的，简单回顾一下两者的差别。

    >>> class AA:
    ...     pass
    ... 

这是定义了一个非常简单的类，而且是旧式类。至于如何定义类，下面会详细说明。读者姑且囫囵吞枣似的的认同我刚才建立的名为`AA`的类，为了简单，这个类内部什么也不做，就是用`pass`一带而过。但不管怎样，是一个类，而且是一个旧式类（或曰经典类）

然后，将这个类实例化（还记得上节中实例化吗？对，就是那个王美女干的事情）：

    >>> aa = AA()
    
不要忘记，实例化的时候，类的名称后面有一对括号。接下来做如下操作：

    >>> type(AA)
    <type 'classobj'>
    >>> aa.__class__
    <class __main__.AA at 0xb71f017c>
    >>> type(aa)
    <type 'instance'>

解读一下上面含义：

- `type(AA)`：查看类`AA`的类型，返回的是`'classobj'`
- `aa.__class__`：aa是一个实例，也是一个对象，每个对象都有`__class__`属性，用于显示它的类型。这里返回的结果是`<class __main__.AA at 0xb71f017c>`，从这个结果中可以读出的信息是，aa是类AA的实例，并且类AA在内存中的地址是`0xb71f017c`。
- `type(aa)`：是要看实例aa的类型，它显示的结果是`'instance`，意思是告诉我们它的类型是一个实例。

在这里是不是有点感觉不和谐呢？`aa.__class__`和`type(aa)`都可以查看对象类型，但是它们居然显示不一样的结果。比如，查看这个对象：

    >>> a = 7
    >>> a.__class__
    <type 'int'>
    >>> type(a)
    <type 'int'>

别忘记了，前面提到过的“万物皆对象”，那么一个整数7也是对象，用两种方式查看，返回的结果一样。为什么到类（严格讲是旧式类）这里，居然返回不一样呢？太不和谐了。

于是乎，就有了新式类，从python2.2开始，变成这样了：

    >>> class BB(object):
    ...     pass
    ... 
    
    >>> bb = BB()
    
    >>> bb.__class__
    <class '__main__.BB'>
    >>> type(bb)
    <class '__main__.BB'>

终于把两者统一起来了，世界和谐了。

这就是新式类和旧式类的不同。

当然，不同点绝非仅仅于此，这里只不过提到一个现在能够理解的不同罢了。另外的不同还在于两者对于多重继承的查找和调用方法不同，旧式类是深度优先，新式类是广度优先。可以先不理解，后面会碰到的。

不管是新式类、还是旧式类，都可以通过这样的方法查看它们在内存中的存储空间信息

    >>> print aa
    <__main__.AA instance at 0xb71efd4c>
    
    >>> print bb
    <__main__.BB object at 0xb71efe6c>

分别告诉了我们两个实例是基于谁生成的，不过还是稍有区别。

知道了旧式类和新式类，那么下面的所有内容，就都是对新式类而言。“喜新厌旧”不是编程经常干的事情吗？所以，旧式类就不是我们讨论的内容了。

还要注意，如果你用的是python3，就不用为新式类和旧式类而担心了，因为在python3中压根儿就没有这个问题存在。

如何定义新式类呢？

第一种定义方法，就是如同前面那样：

    >>> class BB(object):
    ...     pass
    ...

跟旧式类的区别就在于类的名字后面跟上`(object)`，这其实是一种名为“继承”的类的操作，当前的类BB是以类object为上级的（object被称为父类），即BB是继承自类object的新类。在python3中，所有的类自然地都是类object的子类，就不用彰显出继承关系了。对了，这里说的有点让读者糊涂，因为冒出来了“继承”、“父类”、“子类”，不用着急，继续向下看。下面精彩，并且能解惑。

第二种定义方法，在类的前面写上这么一句：`__metaclass__ == type`，然后定义类的时候，就不需要在名字后面写`(object)`了。

    >>> __metaclass__ = type
    >>> class CC:
    ...     pass
    ... 
    >>> cc = CC()
    >>> cc.__class__
    <class '__main__.CC'>
    >>> type(cc)
    <class '__main__.CC'>

两种方法，任你选用，没有优劣之分。

##创建类

因为在一般情况下，一个类都不是两三行能搞定的。所以，下面可能很少使用交互模式了，因为那样一旦有一点错误，就前功尽弃。我改用编辑界面。你用什么工具编辑？python自带一个IDE，可以使用。我习惯用vim。你用你习惯的工具即可。如果你没有别的工具，就用安装python时自带的那个IDE。

    #!/usr/bin/env python
    # coding=utf-8

    __metaclass__ = type

    class Person:
        def __init__(self, name):
            self.name = name

        def getName(self):
            return self.name

        def color(self, color):
            print "%s is %s" % (self.name, color)

上面定义的是一个比较常见的类，一般情况下，都是这样子的。下面对这个“大众脸”的类一一解释。

###新式类

`__metaclass__ = type`，意味着下面的类是新式类。

###定义类

`class Person`，这是在声明创建一个名为"Person"的类。类的名称一般用大写字母开头，这是惯例。如果名称是两个单词，那么两个单词的首字母都要大写，例如`class HotPerson`，这种命名方法有一个形象的名字，叫做“驼峰式命名”。当然，如果故意不遵循此惯例，也未尝不可，但是，会给别人阅读乃至于自己以后阅读带来麻烦，不要忘记“代码通常是给人看的，只是偶尔让机器执行”。既然大家都是靠右走的，你就别非要在路中间睡觉了。
        
接下来，分别以缩进表示的，就是这个类的内容了。其实那些东西看起来并不陌生，你一眼就认出它们了——就是已经学习过的函数。没错，它们就是函数。不过，很多程序员喜欢把类里面的函数叫做“方法”。是的，就是上节中说到的对象的“方法”。我也看到有人撰文专门分析了“方法”和“函数”的区别。但是，我倒是认为这不重要，重要的是类的中所谓“方法”和前面的函数，在数学角度看，丝毫没有区别。所以，你尽可以称之为函数。当然，听到有人说方法，也不要诧异和糊涂。它们本质是一样的。

需要再次提醒，函数的命名方法是以`def`发起，并且函数名称首字母不要用大写，可以使用`aa_bb`的样式，也可以使用`aaBb`的样式，一切看你的习惯了。

不过，要注意的是，类中的函数（方法）的参数跟以往的参数样式有区别，那就是每个函数必须包括`self`参数，并且作为默认的第一个参数。这是需要注意的地方。至于它的用途，继续学习即可知道。

###初始化

`def __init__`，这个函数是一个比较特殊的，并且有一个名字，叫做**初始化函数**（注意，很多教材和资料中，把它叫做构造函数，这种说法貌似没有错误，但是一来从字面意义上看，它对应的含义是初始化，二来在python中它的作用和其它语言比如java中的构造函数还不完全一样，因为还有一个`__new__`的函数，是真正地构造。所以，在本教程中，我称之为初始化函数）。它是以两个下划线开始，然后是init，最后以两个下划线结束。

>所谓初始化，就是让类有一个基本的面貌，而不是空空如也。做很多事情，都要初始化，让事情有一个具体的起点状态。比如你要喝水，必须先初始化杯子里面有水。在python的类中，初始化就担负着类似的工作。这个工作是在类被实例化的时候就执行这个函数，从而将初始化的一些属性可以放到这个函数里面。

此例子中的初始化函数，就意味着实例化的时候，要给参数name提供一个值，作为类初始化的内容。通俗点啰嗦点说，就是在这个类被实例化的同时，要通过name参数传一个值，这个值被一开始就写入了类和实例中，成为了类和实例的一个属性。比如：

    girl = Person('canglaoshi')
   
girl是一个实例对象，就如同前面所说的一样，它有属性和方法。这里仅说属性吧。当通过上面的方式实例化后，就自动执行了初始化函数，让实例girl就具有了name属性。

    print girl.name
    
执行这句话的结果是打印出`canglaoshi`。

这就是初始化的功能。简而言之，通过初始化函数，确定了这个实例（类）的“基本属性”（实例是什么样子的）。比如上面的实例化之后，就确立了实例girl的name是"canglaoshi"。

初始化函数，就是一个函数，所以，它的参数设置，也符合前面学过的函数参数设置规范。比如

    def __init__(self,*args):
        pass

这种类型的参数：*args和前面讲述函数参数一样，就不多说了。忘了的看官，请去复习。但是，self这个参数是必须的。

很多时候，并不是每次都要从外面传入数据，有时候会把初始化函数的某些参数设置默认值，如果没有新的数据传入，就应用这些默认值。比如：

    class Person:
        def __init__(self, name, lang="golang", website="www.google.com"):
            self.name = name
            self.lang = lang
            self.website = website
            self.email = "qiwsir@gmail.com"

    laoqi = Person("LaoQi")     
    info = Person("qiwsir",lang="python",website="qiwsir.github.io")

    print "laoqi.name=",laoqi.name
    print "info.name=",info.name
    print "-------"
    print "laoqi.lang=",laoqi.lang
    print "info.lang=",info.lang
    print "-------"
    print "laoqi.website=",laoqi.website
    print "info.website=",info.website

    #运行结果

    laoqi.name= LaoQi
    info.name= qiwsir
    -------
    laoqi.lang= golang
    info.lang= python
    -------
    laoqi.website= www.google.com
    info.website= qiwsir.github.io

在编程界，有这样一句话，说“类是实例工厂”，什么意思呢？工厂是干什么的？生产物品，比如生产电脑。一个工厂可以生产好多电脑。那么，类，就能“生产”好多实例，所以，它是“工厂”。比如上面例子中，就有两个实例。

###函数（方法）

还是回到本节开头的那个类。构造函数下面的两个函数：`def getName(self)`,`def color(self, color)`，这两个函数和前面的初始化函数有共同的地方，即都是以self作为第一个参数。

    def getName(self):
        return self.name

这个函数中的作用就是返回在初始化时得到的值。

    girl = Person('canglaoshi')
    name = girl.getName()

`girl.getName()`就是调用实例girl的方法。调用该方法的时候特别注意，方法名后面的括号不可少，并且括号中不要写参数，在类中的`getName(self)`函数第一个参数self是默认的，当类实例化之后，调用此函数的时候，第一个参数不需要赋值。那么，变量name的最终结果就是`name = "canglaoshi"`。

同样道理，对于方法：

    def color(self, color):
        print "%s is %s" % (self.name, color)

也是在实例化之后调用：

    girl.color("white")
    
这也是在执行实例化方法，只是由于类中的该方法有两个参数，除了默认的self之外，还有一个color，所以，在调用这个方法的时候，要为后面那个参数传值了。

至此，已经将这个典型的类和调用方法分解完毕，把全部代码完整贴出，请读者在从头到尾看看，是否理解了每个部分的含义：

    #!/usr/bin/env python
    # coding=utf-8

    __metaclass__ = type             #新式类

    class Person:                    #创建类
        def __init__(self, name):    #构造函数
            self.name = name

        def getName(self):           #类中的方法（函数）
            return self.name

        def color(self, color):
            print "%s is %s" % (self.name, color)

    girl = Person('canglaoshi')      #实例化
    name = girl.getName()            #调用方法（函数） 
    print "the person's name is: ", name
    girl.color("white")              #调用方法（函数）

    print "------"
    print girl.name                  #实例的属性
    
保存后，运行得到如下结果：
    
    $ python 20701.py 
    the person's name is:  canglaoshi
    canglaoshi is white
    ------
    canglaoshi
        
###类和实例

有必要总结一下类和实例的关系：

- “类提供默认行为，是实例的工厂”（源自Learning Python），这句话非常经典，一下道破了类和实例的关系。所谓工厂，就是可以用同一个模子做出很多具体的产品。类就是那个模子，实例就是具体的产品。所以，实例是程序处理的实际对象。
- 类是由一些语句组成，但是实例，是通过调用类生成，每次调用一个类，就得到这个类的新的实例。
- 对于类的：`class Person`，class是一个可执行的语句。如果执行，就得到了一个类对象，并且将这个类对象赋值给对象名（比如Person）。

也许上述比较还不足以让看官理解类和实例，没关系，继续学习，在前进中排除疑惑。

##self的作用

类里面的函数，第一个参数是self，但是在实例化的时候，似乎没有这个参数什么事儿，那么self是干什么的呢？

self是一个很神奇的参数。

在Person实例化的过程中`girl = Person("canglaoshi")`，字符串"canglaoshi"通过初始化函数（`__init__()`）的参数已经存入到内存中，并且以Person类型的面貌存在，组成了一个对象，这个对象和变量girl建立引用关系。这个过程也可说成这些数据附加到一个实例上。这样就能够以:`object.attribute`的形式，在程序中任何地方调用某个数据，例如上面的程序中以`girl.name`的方式得到`"canglaoshi"`。这种调用方式，在类和实例中经常使用，点号“.”后面的称之为类或者实例的属性。

这是在程序中，并且是在类的外面。如果在类的里面，想在某个地方使用实例化所传入的数据（"canglaoshi"），怎么办？

在类内部，就是将所有传入的数据都赋给一个变量，通常这个变量的名字是self。注意，这是习惯，而且是共识，所以，看官不要另外取别的名字了。

在初始化函数中的第一个参数self，就是起到了这个作用——接收实例化过程中传入的所有数据，这些数据是初始化函数后面的参数导入的。显然，self应该就是一个实例（准确说法是应用实例），因为它所对应的就是具体数据。

如果将上面的类稍加修改，看看效果：

    #!/usr/bin/env python
    # coding=utf-8

    __metaclass__ = type

    class Person:
        def __init__(self, name):
            self.name = name
            print self           #新增
            print type(self)     #新增

其它部分省略。当初始化的时候，就首先要运行构造函数，同时就打印新增的两条。结果是：

    <__main__.Person object at 0xb7282cec>
    <class '__main__.Person'>

证实了推理。self就是一个实例（准确说是实例的引用变量）。

self这个实例跟前面说的那个girl所引用的实例对象一样，也有属性。那么，接下来就规定其属性和属性对应的数据。上面代码中：
    
    self.name = name

就是规定了self实例的一个属性，这个属性的名字也叫做name，这个属性的值等于初始化函数的参数name所导入的数据。注意，`self.name`中的name和初始化函数的参数`name`没有任何关系，它们两个一样，只不过是一种起巧合（经常巧合，其实是为了省事和以后识别方便，故意让它们巧合。），或者说是写代码的人懒惰，不想另外取名字而已，无他。当然，如果写成`self.xxxooo = name`，也是可以的。

其实，从效果的角度来理解，这么理解更简化：类的实例girl对应着self，girl通过self导入实例属性的所有数据。

当然，self的属性数据，也不一定非得是由参数传入的，也可以在构造函数中自己设定。比如：

    #!/usr/bin/env python
    #coding:utf-8

    __metaclass__ = type
    
    class Person:
        def __init__(self, name):
            self.name = name
            self.email = "qiwsir@gmail.com"     #这个属性不是通过参数传入的

    info = Person("qiwsir")              #换个字符串和实例化变量
    print "info.name=",info.name
    print "info.email=",info.email      #info通过self建立实例，并导入实例属性数据

运行结果

    info.name= qiwsir
    info.email= qiwsir@gmail.com    #打印结果

通过这个例子，其实让我们拓展了对self的认识，也就是它不仅仅是为了在类内部传递参数导入的数据，还能在初始化函数中，通过`self.attribute`的方式，规定self实例对象的属性，这个属性也是类实例化对象的属性，即做为类通过初始化函数初始化后所具有的属性。所以在实例info中，通过info.email同样能够得到该属性的数据。在这里，就可以把self形象地理解为“内外兼修”了。或者按照前面所提到的，将info和self对应起来，self主内，info主外。

怎么样？在"canglaoshi"的陪伴下，是不是明白了类的奥妙？

------

