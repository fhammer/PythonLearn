#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python是动态语言，根据类创建的实例可以任意绑定属性,给实例绑定属性的方法是通过实例变量，或者通过self变量,直接在类中定义的属性成为类属性，也是静态属性

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，
    就变成了一个私有变量（private），只有内部可以访问，外部不能访问

注意: 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
    特殊变量是可以直接访问的，不是private变量

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
    当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
    所以，仍然可以通过_Student__name来访问__name变量,强烈建议你不要这么干

拿到一个对象的引用时，如何知道这个对象是什么类型,使用type()
判断基本数据类型可以直接写int，str,果要判断一个对象是否是函数,可以使用types模块中定义的常量
对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数,能用type()判断的基本类型也可以用isinstance()判断

如果要获得一个对象的所有属性和方法，可以使用dir()函数
"""

import types


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.score = score

    def print_score(self):
        print('%s : %d' % (self.__name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.score = score
        else:
            raise ValueError('bad score')


class Animal(object):
    def run(self):
        print("Animal is running ...")


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


def type_demo():
    animal = Animal()
    dog = Dog()
    cat = Cat()
    print(type(animal))
    print(type(dog))
    print(type(cat))
    print(type(123))
    print(type('123'))
    print(type(123) == type(456))
    # 判断基本数据类型可以直接写int，str
    print(type(123) == int)
    print(type('abc') == type(123))

    # 果要判断一个对象是否是函数,可以使用types模块中定义的常量
    print(type(abs) == types.BuiltinFunctionType)
    print(type(run_twice) == types.FunctionType)
    print(type(lambda x: x) == types.LambdaType)
    print(type((x for x in range(10))) == types.GeneratorType)
    # 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
    print(isinstance(dog, Animal))
    print(isinstance(dog, Dog))
    print(isinstance(dog, Cat))
    # 能用type()判断的基本类型也可以用isinstance()判断
    print(isinstance('123', str))
    print(isinstance(123, int))
    print(isinstance(b'a', bytes))
    # 还可以判断一个变量是否是某些类型中的一种
    print(isinstance([1, 2, 3], (list, tuple)))


class MyAttr(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


def attr_func(obj):
    if hasattr(obj, 'x'):
        print(obj.x)
    if hasattr(obj, 'y'):
        print(obj.y)
    else:
        setattr(obj, 'y', 19)
    # 如果试图获取不存在的属性，会抛出AttributeError的错误,getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
    print(getattr(obj, 'y'))


class Person(object):
    name = 'hammer'

    def __init__(self):
        self.age = 18

    def get_info(self):
        print(self.name, self.age)


def static_attr():
    print(Person.name)
    p = Person()
    print(p.name)
    print(p.age)
    p.get_info()


if __name__ == "__main__":
    # stu = Student('Nance', 100)
    # stu.print_score()
    # print(stu.score)
    # print(stu._Student__name)
    # animal = Animal()
    # dog = Dog()
    # cat = Cat()
    # dog.run()
    # cat.run()
    # run_twice(animal)
    # run_twice(dog)
    # run_twice(cat)
    # type_demo()
    # print(dir('abd'))
    #
    # obj = MyAttr()
    # attr_func(obj)

    static_attr()
