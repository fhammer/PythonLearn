# coding=utf-8
import os

# movie_name = os.listdir('E:/3x')
# for temp in movie_name:
#     new_name = 'ic_shop_' + temp
#     os.rename('E:/3x/' + temp, 'E:/3x/' + new_name)

movie_name = os.listdir('E:/3x')
for temp in movie_name:
    num = temp.rfind('.')  # 找到最右边]的下标
    # new_name = '[可可可可]' + temp
    new_name = (temp[:num - 3] + ".png")
    new_name = new_name.replace("-hover", "")
    os.rename('E:/3x/' + temp, 'E:/3x/' + new_name)
