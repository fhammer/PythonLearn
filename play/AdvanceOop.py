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


if __name__ == "__main__":
    stu = Student()
    stu.score = 10
    print(stu.score)
