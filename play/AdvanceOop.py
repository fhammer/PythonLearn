#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python 动态的绑定属性和方法对另一个实例是不起作用的，需要对类进行绑定

Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
    __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__

@property装饰器就是负责把一个方法变成属性调用
"""


# class Student(object):
#     __slots__ = ('name', 'age')


# class Student(object):
#     def get_score(self):
#         return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class Person(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'Person object (name: %s)' % self.__name

    # __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
    __repr__ = __str__


"""
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
"""


class FibItr(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


def fib_fun():
    for x in FibItr():
        print(x)


class FibArray(object):
    # 支持fast-fail的数组定制类
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


class FibArraySlice(object):
    # 支持切片和fast-fail的数组定制类
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


def fib_array_func():
    print(FibArray()[5])


from enum import Enum


if __name__ == "__main__":
    stu = Student()
    stu.score = 10
    print(stu.score)
    print(stu)

    p = Person('hammer')
    print(p)
    # fib_fun()
    fib_array_func()

    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)
