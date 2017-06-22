#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame

array1 = np.arange(12).reshape((3, 4))
print(array1, end='\n\r\n\r')
df1 = DataFrame(array1, columns=list('abcd'))
print(df1, end='\n\r\n\r')

df2 = DataFrame(np.arange(20).reshape(4, 5), columns=list('abcde'))
print(df2, end='\n\r\n\r')

print(df1 + df2, end='\n\r\n\r')

df3 = df2.reindex(index=range(6), columns=list('bdfhi'), method='ffill')
print(df3)

df4 = df2.reindex(index=range(6), columns=list('bdfhij'), fill_value=0)
print(df4)
