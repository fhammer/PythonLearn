#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

list() list函数用于将一个惰性的序列完成计算然后返回list，range filter这些函数返回都是惰性序列
map() map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
reduce() reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
        filter函数关键在于正确实现一个“筛选”函数
sorted()函数就可以对list进行排序

高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回,闭包（Closure）
返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量
如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变

匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

"""

import functools
import play.PlayTest

__author__ = 'fhammer'


def add_func(a, b, f):
    return f(a) + f(b);


def red_fun(x, y):
    print('x= ', x, 'y= ', y)
    return x * 10 + y


def print_reduce():
    print(functools.reduce(red_fun, [1, 3, 5, 7, 9]))


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return functools.reduce(fn, map(char2num, s))


def filter_fun():
    def is_odd(num):
        return num % 2 == 1

    return list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))


def filter_empty():
    def not_empty(s):
        return s and s.strip()

    return list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


def count():
    # 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


def count_arg():
    # 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


def count_fun():
    # 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量
    # 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
    f1, f2, f3 = count()
    print(f1())
    print(f2())
    print(f3())


def count_fun_arg():
    f1, f2, f3 = count_arg()
    print(f1())
    print(f2())
    print(f3())


"""
装饰器
函数对象有一个__name__属性，可以拿到函数的名字
decorator就是一个返回函数的高阶函数,接受一个函数作为参数，并返回一个函数。借助Python的@语法，把decorator置于函数的定义处
"""


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    # 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
    # 原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数
    print('2015-3-25')


def log_txt(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log_txt('python_hammer')
def now_txt():
    # 相当于执行了now = log('execute')(now)
    # 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
    print('2015-3-25')


def log_perfect(func):
    # 把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


def log_txt_perfect(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


def int2(x, base=2):
    return int(x, base)


def partial_fun():
    # functools.partial就是帮助我们创建一个偏函数的
    # functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
    return functools.partial(int, base=8)


def test_partial():
    print(int2('12', 8))
    print(partial_fun()('12'))


if __name__ == '__main__':
    # print(add_func(-5, 6, abs))
    # print_reduce()
    # print(filter_fun())
    # print(filter_empty())
    # print(sorted([36, 5, -12, 9, -21], key=abs))
    # print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
    # print(lazy_sum(1, 3, 5, 7, 9))
    # print(lazy_sum(1, 3, 5, 7, 9)())
    # count_fun_arg()
    now()
    now_txt()
    test_partial()
    play.PlayTest.say_hello('kkkkkkkk')
