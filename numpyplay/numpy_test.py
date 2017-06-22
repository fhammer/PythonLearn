#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy

# 从数值类型构造
print(numpy.dtype(float))

# 从字符代码构造
print(numpy.dtype('f'))
print(numpy.dtype('d'))

# 从双字符代码构造
print(numpy.dtype('f8'))

# 获取所有字符代码
print(numpy.sctypeDict.keys())

# char 属性获取字符代码
t = numpy.dtype('Float64')
print(t.char)
# type 属性获取类型
print(t.type)
# str 属性获取完整字符串表示
# 第一个字符是字节序，< 表示小端，> 表示大端，| 表示平台的字节序
print(t.str)
# 获取大小
print(t.itemsize)

# 许多函数拥有 dtype 参数
# 传入数值类型、字符代码和 dtype 都可以
print(numpy.arange(7, dtype=numpy.uint16))

# 创建多维数组
m = numpy.array([numpy.arange(2), numpy.arange(2)])
print(m)
# 打印形状
print(m.shape)

# 创建 2x2 的矩阵
a = numpy.array([[1, 2], [3, 4]])
print(a)

setss = {'jjj', 'jjjj'}
sets = set(['jjjj', 'llllllll'])
print(setss, sets)
