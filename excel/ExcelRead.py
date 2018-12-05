# -*- coding: utf-8 -*-
import xlrd
import pandas as pd
import numpy as np
import xlwt
from tqdm import tqdm
from datetime import date, datetime


def pandas_read_data():
    pd_data =  pd.DataFrame(pd.read_excel(r"E:\CN-CID.xlsx"))
    print(pd_data.shape)
    # print(pd_data.info())
    # print(pd_data['Terms'].dtype)
    # print(pd_data.head(6))

    df_searise=pd_data['Terms']
    df_values_count=df_searise.value_counts()
    print(df_values_count)
    df_values_count.to_csv(r"./csv/terms_count.csv")

    pd_data['Sentiment'].value_counts().to_csv(r"./csv/Sentiment.csv")
    pd_data['vTaxonomyLevel'].value_counts().to_csv(r"./csv/vTaxonomyLevel.csv")
    pd_data['Sub-category'].value_counts().to_csv(r"./csv/Sub-category.csv")
    pd_data['Product'].value_counts().to_csv(r"./csv/Product.csv")
    pd_data['Business Group'].value_counts().to_csv(r"./csv/Business_Group.csv")


def read_data():
    xl_datas = xlrd.open_workbook(r"E:\CID.xlsx")
    if xl_datas.sheets():
        sheet_table=xl_datas.sheets()[0]
        print(sheet_table.nrows)
        print(sheet_table.ncols)
        col = sheet_table.col_values(3)
        print(col)
        for item_data in range(sheet_table.nrows):
            print("%d, = %s " %(item_data,col[item_data]))
    else:
        print("==============Error==============")
        return


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'E:\Codata.xlsx')
    # 获取所有sheet
    sheets=workbook.sheet_names()  # [u'sheet1', u'sheet2']
    for shrrtItem in sheets:
        print(shrrtItem)
    sheet2_name = workbook.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(0)  # sheet索引从0开始
    # sheet2 = workbook.sheet_by_name(sheet2)
    # sheet的名称，行数，列数
    print(sheet2.name, sheet2.nrows, sheet2.ncols)
    # 获取整行和整列的值（数组）
    rows = sheet2.row_values(3)  # 获取第四行内容
    cols = sheet2.col_values(2)  # 获取第三列内容
    print(rows)
    print(cols)
    # 获取单元格内容
    # print(sheet2.cell(1, 0).value.encode('utf-8'))
    # print(sheet2.cell_value(1, 0).encode('utf-8'))
    # print(sheet2.row(1)[0].value.encode('utf-8'))
    # 获取单元格内容的数据类型
    print(sheet2.cell(1, 0).ctype)

if __name__ == '__main__':
    pandas_read_data()