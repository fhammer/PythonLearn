# -*- coding: utf-8 -*-


def say_hello(arg):
    print(arg)


def say_hex(arg):
    # 转换一个数字为16进制
    print(hex(arg))


def say_hex_s():
    # 循环输出十六进制数字
    for x in range(17):
        say_hex(x)


def my_abs(x):
    # 进行类型判断的函数
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def power(x, n):
    print(x ** n)


def calc(*numbers):
    # 可变参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def enroll(name, gender, age=6, city="BJ"):
    # 默认参数的函数，牢记一点：默认参数必须指向不变对象
    print(name, gender, age, city)


def person(name, age, **kw):
    # 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
    print('name:', name, 'age:', age, 'other:', kw)


def name_arg(name, age, *, city, job):
    # 命名关键字参数,限制关键字参数的名字
    print(name, age, city, job)


def name_args(name, age, *args, city, job):
    # 函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
    print(name, age, args, city, job)


if __name__ == "__main__":
    say_hello("Hi Python Idea")
    say_hex_s()
    power(2, 4)
    # 可变参数
    enroll('Hammer', 'M', 7)
    enroll('Janet', 'M', 8, 'XC')
    enroll('Nance', 'M', city='HN')
    # 可变参数
    nums = [1, 2, 3]
    say_hello(calc(*nums))
    say_hello(calc(1, 2, 3, 4, 5))
    # 关键字参数
    person('hammer', 10)
    person('hammer', 10, city='BJ')
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, **extra)
    name_args('name', 10, city='BJ', job='SD')
    name_args('name', 10, 1, 2, 3, city='BJ', job='SD')
    print('你是上述三和十四大东hdhd'[0: 12])
