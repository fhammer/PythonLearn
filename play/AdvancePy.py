#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable
import os


def substring(str):
    print(str[:-1:3])


def iterables(ob):
    return isinstance(ob, Iterable)


def for_each_item(items):
    for index, value in enumerate(items):
        print(index, " = ", value)


def for_each_arrays(obs):
    for x, y in obs:
        print(x, y)


def produce_list():
    return [x ** 2 for x in range(1, 19) if x % 2 == 0]


def mut_list():
    return [m + n for m in 'ABC' for n in 'XYZ']


def list_dir():
    return [d for d in os.listdir('../')]


def list_direct():
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    return [k + '=' + v for k, v in d.items()]


'''
下面是生成器部分，一边循环一边计算的机制，称为生成器：generator。generator也是可迭代对象
它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令
'''


def generator_list():
    # 一个简单的生成器，和生成式的区别很明显 [] 换成了()
    return (x * x for x in range(10))


def generator_items(gen):
    # 取出生成器的下一个元素
    return next(gen)


def fib(max):
    # 当生成器不能很好的写出某一个算法时 可以用函数代替
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


def odd():
    # 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，
    # 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


def fib_gen(max):
    # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
    # 将函数改写成生成器
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def get_return_value(g):
    # 拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
    while True:
        try:
            x = next(g)
            print('g= ', x)
        except StopIteration as e:
            print('生成器的返回值是: ', e.value)
            break


def triangles():
    # 杨辉三角的生成器算法, 大致思路是每次在数组后追加一个0，下一行的每个元素等于上一个数组的强两个元素的和
    array = [1]
    while True:
        yield array
        array.append(0)
        array = [array[i - 1] + array[i] for i in range(len(array))]


def triangles_items():
    # 用于迭代杨辉三角的每一行元素
    n = 0
    for m in triangles():
        print(m)
        n = n + 1
        if n == 10:
            break


if __name__ == "__main__":
    # substring('你是上述三和十四大东hdhd')
    # print(iterables('jjj'))
    # print(iterables([1, 2]))
    # for_each_item(['A', 'B', 'C'])
    # for_each_arrays([(1, 1), (2, 4), (3, 9)])
    # for_each_item(range(1, 11))
    # for_each_item(produce_list())
    # for_each_item(mut_list())
    # for_each_item(list_dir())
    # for_each_item(list_direct())
    # print(generator_items(generator_list()))
    # for_each_item(generator_list())
    # fib(10)
    # for_each_item(fib_gen(10))
    # for_each_item(odd())
    # get_return_value(fib_gen(12))
    triangles_items()
