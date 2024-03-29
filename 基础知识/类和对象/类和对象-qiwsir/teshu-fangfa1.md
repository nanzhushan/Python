>我们既蒙怜悯，受了这职分，就不丧胆，乃将那些暗昧可耻的事弃绝了，不行诡诈，不谬讲神的道理，只将真理表明出来，好在神面前把自己荐与各人的良心。(2 CORINTHIANS 4:1-2)

#特殊方法(1)

探究更多的类属性，在一些初学者的教程中，一般很少见。我之所以要在这里也将这部分奉献出来，就是因为本教程是“From Beginner to Master”。当然，不是学习了类的更多属性就能达到Master水平，但是这是通往Master的一步，虽然在初级应用中，本节乃至于后面关于类的属性用的不很多，但是，这一步迈出去，你就会在实践中有一个印象，以后需要用到了，知道有这一步，会对项目有帮助的。俗话说“艺不压身”。

##`__dict__`

前面已经学习过有关类属性和实例属性的内容，并且做了区分，如果忘记了可以回头参阅[《类(3)》](./208.md)中的“类属性和实例属性”部分。有一个结论，是一定要熟悉的，那就是可以通过`object.attribute`的方式访问对象的属性。

如果接着那部分内容，读者是否思考过一个问题：类或者实例属性，在python中是怎么存储的？或者为什么修改或者增加、删除属性，我们能不能控制这些属性？

    >>> class A(object):
    ...     pass
    ...
    
    >>> a = A()
    >>> dir(a)
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
    >>> dir(A)
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

用`dir()`来查看一下，发现不管是类还是实例，都有很多属性，这在前面已经反复出现，有点见怪不怪了。不过，这里我们要看一个属性：`__dict__`，因为它是一个保存秘密的东西：对象的属性。

    >>> class Spring(object):
    ...     season = "the spring of class"
    ... 

    >>> Spring.__dict__
    dict_proxy({'__dict__': <attribute '__dict__' of 'Spring' objects>, 
    'season': 'the spring of class', 
    '__module__': '__main__', 
    '__weakref__': <attribute '__weakref__' of 'Spring' objects>, 
    '__doc__': None})

为了便于观察，我将上面的显示结果进行了换行，每个键值对一行。

对于类Spring的`__dict__`属性，可以发现，有一个键`'season'`，这就是这个类的属性；其值就是类属性的数据。
    
    >>> Spring.__dict__['season']
    'the spring of class'
    >>> Spring.season
    'the spring of class'

用这两种方式都能得到类属性的值。或者说`Spring.__dict__['season']`就是访问类属性。下面将这个类实例化，再看看它的实例属性：
    
    >>> s = Spring()
    >>> s.__dict__
    {}

实例属性的`__dict__`是空的。有点奇怪？不奇怪，接着看：

    >>> s.season
    'the spring of class'

这个其实是指向了类属性中的`Spring.season`，至此，我们其实还没有建立任何实例属性呢。下面就建立一个实例属性：

    >>> s.season = "the spring of instance"
    >>> s.__dict__
    {'season': 'the spring of instance'}
    
这样，实例属性里面就不空了。这时候建立的实例属性和上面的那个`s.season`只不过重名，并且把它“遮盖”了。这句好是不是熟悉？因为在讲述“实例属性”和“类属性”的时候就提到了。现在读者肯定理解更深入了。

    >>> s.__dict__['season']
    'the spring of instance'
    >>> s.season
    'the spring of instance'

此时，那个类属性如何？我们看看：

    >>> Spring.__dict__['season']
    'the spring of class'
    >>> Spring.__dict__
    dict_proxy({'__dict__': <attribute '__dict__' of 'Spring' objects>, 'season': 'the spring of class', '__module__': '__main__', '__weakref__': <attribute '__weakref__' of 'Spring' objects>, '__doc__': None})
    >>> Spring.season
    'the spring of class'

Spring的类属性没有受到实例属性的影响。

按照前面的讲述类属性和实例熟悉的操作，如果这时候将前面的实例属性删除，会不会回到实例属性`s.__dict__`为空呢？

    >>> del s.season
    >>> s.__dict__
    {}
    >>> s.season
    'the spring of class'

果然打回原形。

当然，你可以定义其它名称的实例属性，它一样被存储到`__dict__`属性里面：

    >>> s.lang = "python"
    >>> s.__dict__
    {'lang': 'python'}
    >>> s.__dict__['lang']
    'python'

诚然，这样做仅仅是更改了实例的`__dict__`内容，对`Spring.__dict__`无任何影响，也就是说通过`Spring.lang`或者`Spring.__dict__['lang']`是得不到上述结果的。

    >>> Spring.lang
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: type object 'Spring' has no attribute 'lang'
    
    >>> Spring.__dict__['lang']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'lang'

那么，如果这样操作，会怎样呢？

    >>> Spring.flower = "peach"
    >>> Spring.__dict__
    dict_proxy({'__module__': '__main__', 
    'flower': 'peach', 
    'season': 'the spring of class', 
    '__dict__': <attribute '__dict__' of 'Spring' objects>, '__weakref__': <attribute '__weakref__' of 'Spring' objects>, '__doc__': None})
    >>> Spring.__dict__['flower']
    'peach'

在类的`__dict__`被更改了，类属性中增加了一个'flower'属性。但是，实例的`__dict__`中如何？
    
    >>> s.__dict__
    {'lang': 'python'}
    
没有被修改。我也是这么想的，哈哈。你此前这这么觉得吗？然而，还能这样：

    >>> s.flower
    'peach'

这个读者是否能解释？其实又回到了前面第一个出现`s.season`上面了。

通过上面探讨，是不是基本理解了实例和类的`__dict__`，并且也看到了属性的变化特点。特别是，这些属性都是可以动态变化的，就是你可以随时修改和增删。

属性如此，方法呢？下面就看看方法（类中的函数）。

    >>> class Spring(object):
    ...     def tree(self, x):
    ...         self.x = x
    ...         return self.x
    ... 
    >>> Spring.__dict__
    dict_proxy({'__dict__': <attribute '__dict__' of 'Spring' objects>, 
    '__weakref__': <attribute '__weakref__' of 'Spring' objects>, 
    '__module__': '__main__', 
    'tree': <function tree at 0xb748fdf4>, 
    '__doc__': None})

    >>> Spring.__dict__['tree']
    <function tree at 0xb748fdf4>

结果跟前面讨论属性差不多，方法`tree`也在`__dict__`里面呢。

    >>> t = Spring()
    >>> t.__dict__
    {}

又跟前面一样。虽然建立了实例，但是在实例的`__dict__`中没有方法。接下来，执行：
    
    >>> t.tree("xiangzhangshu")
    'xiangzhangshu'

在[类(3)](./208.md)中有一部分内容阐述“数据流转”，其中有一张图，其中非常明确显示出，当用上面方式执行方法的时候，实例`t`与`self`建立了对应关系，两者是一个外一个内。在方法中`self.x = x`，将x的值给了self.x，也就是实例应该拥有了这么一个属性。

    >>> t.__dict__
    {'x': 'xiangzhangshu'}

果然如此。这也印证了实例`t`和`self`的关系，即实例方法(`t.tree('xiangzhangshu')`)的第一个参数(self，但没有写出来)绑定实例t，透过self.x来设定值，即给`t.__dict__`添加属性值。

换一个角度：

    >>> class Spring(object):
    ...     def tree(self, x):
    ...         return x
    ...

这回方法中没有将x赋值给self的属性，而是直接return，结果是：
    
    >>> s = Spring()
    >>> s.tree("liushu")
    'liushu'
    >>> s.__dict__
    {}

是不是理解更深入了？

现在需要对python中一个观点：“一切皆对象”，再深入领悟。以上不管是类还是的实例的属性和方法，都是符合`object.attribute`格式，并且属性类似。

当你看到这里的时候，要么明白了类和实例的`__dict__`的特点，要么就糊涂了。糊涂也不要紧，再将上面的重复一遍，特别是自己要敲一敲有关代码。（建议一个最好的方法：用两个显示器，一个显示器看本教程，另外一个显示器敲代码。事半功倍的效果。）

需要说明，我们对`__dict__`的探讨还留有一个尾巴：属性搜索路径。这个留在后面讲述。

不管是类还是实例，其属性都能随意增加。这点在有时候不是一件好事情，或许在某些时候你不希望别人增加属性。有办法吗？当然有，请继续学习。

##`__slots__`

首先声明，`__slots__`能够限制属性的定义，但是这不是它存在终极目标，它存在的终极目标更应该是一个在编程中非常重要的方面：**优化内存使用。**

    >>> class Spring(object):
    ...     __slots__ = ("tree", "flower")
    ... 
    >>> dir(Spring)
    ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', 'flower', 'tree']

仔细看看`dir()`的结果，还有`__dict__`属性吗？没有了，的确没有了。也就是说`__slots__`把`__dict__`挤出去了，它进入了类的属性。

    >>> Spring.__slots__
    ('tree', 'flower')

这里可以看出，类Spring有且仅有两个属性。

    >>> t = Spring()
    >>> t.__slots__
    ('tree', 'flower')

实例化之后，实例的`__slots__`与类的完全一样，这跟前面的`__dict__`大不一样了。

    >>> Spring.tree = "liushu"

通过类，先赋予一个属性值。然后，检验一下实例能否修改这个属性：

    >>> t.tree = "guangyulan"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'Spring' object attribute 'tree' is read-only

看来，我们的意图不能达成，报错信息中显示，`tree`这个属性是只读的，不能修改了。

    >>> t.tree
    'liushu'

因为前面已经通过类给这个属性赋值了。不能用实例属性来修改。只能：

    >>> Spring.tree = "guangyulan"
    >>> t.tree
    'guangyulan'
    
用类属性修改。但是对于没有用类属性赋值的，可以通过实例属性：

    >>> t.flower = "haitanghua"
    >>> t.flower
    'haitanghua'
    
但此时：

    >>> Spring.flower
    <member 'flower' of 'Spring' objects>

实例属性的值并没有传回到类属性，你也可以理解为新建立了一个同名的实例属性。如果再给类属性赋值，那么就会这样了：

    >>> Spring.flower = "ziteng"
    >>> t.flower
    'ziteng'

当然，此时在给`t.flower`重新赋值，就会爆出跟前面一样的错误了。

    >>> t.water = "green"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'Spring' object has no attribute 'water'

这里试图给实例新增一个属性，也失败了。

看来`__slots__`已经把实例属性牢牢地管控了起来，但更本质是的是优化了内存。诚然，这种优化会在大量的实例时候显出效果。

------
