#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
正常的函数和变量名是公开的（public），可以被直接引用
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途,文档注释也可以用特殊变量__doc__访问
类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用,
    而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量
外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public
"""
from PIL import Image
import sys

__author__ = 'fhammer'


def image_thump():
    im = Image.open(r'C:\Users\fuzh2\Desktop\学习\学习笔记\Python\10.png')
    print(im.format, im.size, im.mode)
    im.thumbnail((200, 200))
    im.save(r'C:\Users\fuzh2\Desktop\学习\学习笔记\Python\10_thumb.jpg', 'JPEG')

if __name__ == '__main__':
    image_thump()
    print(sys.path)
