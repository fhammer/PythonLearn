#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict


def timedate_func():
    print(datetime.datetime.now())
    print(datetime.datetime.now().strftime('%a, %b %d %H:%M'))
    dt = datetime.datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
    print(dt)
    print(dt.timestamp())
    print(datetime.datetime.fromtimestamp(dt.timestamp()))
    print(datetime.datetime.utcfromtimestamp(dt.timestamp()))
    cday = datetime.datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
    print(cday)

    now = datetime.datetime.now()
    print(now)
    print(now + datetime.timedelta(hours=2))
    print(now + datetime.timedelta(hours=2, minutes=20))


def collections_fun():
    # namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x, p.y)
    print(isinstance(p, Point))
    print(isinstance(p, tuple))
    # deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
    q = deque(['a', 's', 'f'])
    q.append('c')
    q.appendleft('1')
    for x in q:
        print(x)

    # 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'
    print(dd['key1'])
    print(dd['key2'])

    # 使用dict时，Key是无序的,如果要保持Key的顺序，可以用OrderedDict
    d = dict([('a', 1), ('b', 2), ('c', 3)])
    print(d)
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(od)


class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


def Foo():
    i=0
    def fc():
        i=i+1
        print(i)
    return fc

if __name__ == "__main__":
    # timedate_func()
    collections_fun()
    f1=Foo()
    f2=Foo()
    f1()
    f1()
