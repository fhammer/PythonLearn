#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
这一部分是来练习文件操作的部分

文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。
"""

from io import StringIO
from io import BytesIO
import os


class FileIoFunc(object):
    def open_file(self):
        try:
            file = open(r'./FileIO.py', 'r', errors='ignore')
            # read()方法可以一次读取文件的全部内容
            print(file.read())
        finally:
            if file:
                file.close()

    def with_file(self):
        # 和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法
        with open(r'./FileIO.py', 'r', encoding='utf-8') as file:
            print(file.read())

    def read_lines(self):
        with open(r'./FileIO.py', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                print(line.strip())  # 把末尾的'\n'删掉


class StringIoFunc(object):
    def io_write(self):
        sIo = StringIO()
        print(sIo.write('Hello,hammer'))
        # getvalue()方法用于获得写入后的str
        print(sIo.getvalue())

    def io_read(self):
        io_str = StringIO('写入 ni shi da sha b ')
        while True:
            s = io_str.readline()
            if s == '':
                break
            print(s)


class BytesIoFun(object):
    def byte_write(self):
        byte_io = BytesIO()
        print(byte_io.write(b'hhhhhhhhh'))
        print(byte_io.write('得写入hhhhhhhhh'.encode('utf-8')))
        print(byte_io.getvalue())

    def byte_read(self):
        byte_io = BytesIO(b'-----------------')
        print(byte_io.read())


import shutil


class OSFunc(object):
    def os_cmd(self):
        print(os.name)
        # uname() 在windows下面不提供
        # print(os.uname())
        print(os.uname_result)
        print(os.environ)
        print(os.environ.get('JAVA_HOME'))

    def os_order_dir(self):
        # 查看当前目录的绝对路径:
        print(os.path.abspath('.'))
        # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
        # 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
        # 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
        # t_path = os.path.join(r'D:\123', 'testdir')
        # print(t_path)
        # 然后创建一个目录:
        # os.mkdir(t_path)
        # 删掉一个目录:
        # os.rmdir(t_path)
        files = [x for x in os.listdir(r'D:\123') if os.path.isdir(x)]
        for f in files:
            print(f)

        print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

        shutil.copy(r'D:\123\123.sh', r'D:\123\testdir')


if __name__ == '__main__':
    # fileFun = FileIoFunc()
    # fileFun.open_file()
    # with_file()
    # read_lines()

    # s_io = StringIoFunc()
    # s_io.io_write()
    # s_io.io_read()

    # byte_io = BytesIoFun()
    # byte_io.byte_write()
    # byte_io.byte_read()

    os_func = OSFunc()
    os_func.os_cmd()
    os_func.os_order_dir()
