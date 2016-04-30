#coding:utf-8
#用上一个代码，的确做到了封装。但是，我如果要调用那些私有属性，怎么办？

__metaclass__ = type

class Protectme:
    def __init__(self):
        self.me = 'knight'
        self.__name = 'zhoulong'

#调用私有属性，使用@property来实现               

    @property
    def name(self):
        return self.__name
    
if __name__ == "__main__":
    p = Protectme()
    print p.name