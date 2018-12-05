import warnings
import regex as re
import numpy as np
import math
import pandas as pd
import jieba
from tqdm import tqdm

import jieba.analyse
import pymysql
import sys
import os

# src_file_path = sys.argv[1]


def xls_to_db(file_path, index_key):
    data = pd.DataFrame(pd.read_excel(r"E:\CorpusWordlist.xls"))
    # data = pd.read_csv(file_path, encoding='utf-8', names=['A', 'B'])
    duanzi = ''  # 初始化字符串
    for i in range(data.shape[0]):  # 数字为数据的行数
        index = data.ix[i, :]  # 取每行
        content = index['B']  # 取每行的question
        print(content)
        duanzi = duanzi + content

    # 创建连接
    conn = pymysql.connect(host='1.20.5.13', port=3306, user='user', passwd='password', db='club', charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    tags = jieba.analyse.extract_tags(duanzi, topK=100, withWeight=True)
    for item in tags:
        print(item[0] + '\t' + str(int(item[1] * 1000)))
        # 执行SQL，并返回受影响行数,执行多次
        # effect_row = cursor.executemany("insert into ai_newwords(stat_date,word,count)values(%s,%s,%s)",
        #                                 [(index_key, item[0], item[1] * 1000)])
        try:
            effect_row = cursor.executemany("insert into ai_words_dict(word)values(%s)",[(item[0])])
            conn.commit()
        except :
            # print('insert into ai_newwords  VALUES(?,?,?) WHERE NOT EXISTS(SELECT stat_date,word from ai_newwords where stat_date=? AND word = ?)')
            print("============Insert Error============")
            pass
    print("=================\n")
    # 提交，不然无法保存新建或者修改的数据
    # conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    # print(data[1].head(10))


if __name__ == "__main__":
    data = pd.DataFrame(pd.read_excel(r"E:\CorpusWordlist.xls"))
    print(data.shape)
    print(data.columns)
    # 创建连接
    conn = pymysql.connect(host='1.20.5.3', port=3306, user='user', passwd='password', db='club', charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    for name in data['Unnamed: 1']:
        print(name)
        # 执行SQL，并返回受影响行数,执行多次
        # effect_row = cursor.executemany("insert into ai_newwords(stat_date,word,count)values(%s,%s,%s)",
        #                                 [(index_key, item[0], item[1] * 1000)])
        try:
            effect_row = cursor.executemany("insert into ai_words_dict(word)values(%s)",
                                            [(name)])
        except:
            print("============Insert Error============")
            pass
    print("=================\n")
    # 提交，不然无法保存新建或者修改的数据
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
