#coding:utf-8
'''
迭代器的确有迷人之处，但是它也不是万能之物。比如迭代器不能回退，只能如过河的卒子，不断向前。
另外，迭代器也不适合在多线程环境中对可变集合使用（这句话可能理解有困难，先混个脸熟吧，等你遇到多线程问题再说）。
'''

__metaclass__ = type

class Fibs:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):              #迭代器
        fib = self.a
        if fib > self.max: 
            raise StopIteration      ##raise异常处理
        self.a, self.b = self.b, self.a + self.b
        return fib

if __name__ == "__main__":
    fibs = Fibs(5)
    print list(fibs)
    
    
'''
__iter__()是类中的核心，它返回了迭代器本身。一个实现了__iter__()方法的对象，即意味着其实可迭代的。
含有next()的对象，就是迭代器，并且在这个方法中，在没有元素的时候要发起StopIteration()异常。
'''
    