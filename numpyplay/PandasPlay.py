#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd

obj = pd.Series([2, 3, 5, 7])
print(obj)

dic = {'a': 1, 'b': 3, 'c': 7}
obj2 = pd.Series(dic)
print(obj2)

obj3 = pd.Series([2, 3, 5, 7], index=['w', 'q', 'r', 'u'])
print(obj3)

print(obj3['q'])
print(obj3[['q', 'q']])
obj3['w'] = 12
obj3[['r', 'q']] = 18
print(obj3)

print(obj3.index)
print(obj3.items)
print(obj3.values)

obj3 = obj3 + 1
print(obj3)
print(obj3[obj3 <= 10])
print(obj3[obj3 > 10])

data = {
    'id': '1202',
    'type': 1,
    'sort': 1,
    'update_time': 1497251379800,
    'version': 111,
    'display_new': 0,
    'pic': 'http://clubimg.lenovo.com.cn/pic/6756854894785/0',
    'txt': 1234,
    'url': 1117777679103260,
    'ext_info':''
}

fram = pd.DataFrame(data)
print(fram)

