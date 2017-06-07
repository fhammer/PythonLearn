#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
这一部分是来练习文件操作的部分

文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。
"""


def open_file():
    try:
        file = open(r'./FileIO.py', 'r', errors='ignore')
        # read()方法可以一次读取文件的全部内容
        print(file.read())
    finally:
        if file:
            file.close()


def with_file():
    # 和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法
    with open(r'./FileIO.py', 'r', encoding='utf-8') as file:
        print(file.read())


def read_lines():
    with open(r'./FileIO.py', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            print(line.strip()) # 把末尾的'\n'删掉


if __name__ == '__main__':
    open_file()
    # with_file()
    # read_lines()