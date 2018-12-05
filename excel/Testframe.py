import numpy as np
import pandas as pd

data = {'city': ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Hangzhou', 'Chongqing'],
        'year': [2016, 2016, 2015, 2017, 2016, 2016],
        'population': [2100, 2300, 1000, 700, 500, 500]}
frame = pd.DataFrame(data, columns=['year', 'city', 'population', 'debt'])

frame.to_csv(r'./csv/test.csv', header=False, index=False)


def function(a, b):
    if 'ing' in a and b == 2016:
        return 1
    else:
        return 0


print(frame, '\n')
frame['test'] = frame.apply(lambda x: function(x.city, x.year), axis=1)
print(frame)


def str_sub(str):
    return str.replace(str[2:6], "")


def str_sub_2(str):
    strs = str.split(r'/')
    return strs[2] + strs[0]


print(str_sub_2("06/29/2017"))
