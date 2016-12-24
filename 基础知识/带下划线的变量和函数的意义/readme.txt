1 变量:

常量 : 大写加下划线 （表示不会改变的常量）
e.g  USER_CONSTANT

私有变量： 小写和一个前导下划线
e.g  _pva

内置变量: 小写，两个前导下划线和两个后置下划线,比如 __doc__  等
__class__




2 函数：
  
私有方法 ： 小写和一个前导下划线

def _secrete(self):
    print "don't test me"


特殊方法或者魔法方法:   小写和两个前导下划线，两个后置下划线

def __add__(self, other):
    return int.__add__(other)