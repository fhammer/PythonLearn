# -*- coding: utf-8 -*-
import xlrd
import pandas as pd
import time
import sys


# src_file_path = sys.argv[1]
# out_file_dir = sys.argv[2]
#
# print(src_file_path)
# print(out_file_dir)


def read_data():
    xl_datas = xlrd.open_workbook(r"C:\Desktop\201810\ContactUsOptionsTiles(20181101).xlsx")
    if xl_datas.sheets():
        sheet_table = xl_datas.sheets()[0]
        print(sheet_table.nrows)
        print(sheet_table.ncols)
        col = sheet_table.col_values(3)
        print(col)
        for item_data in range(sheet_table.nrows):
            print("%d, = %s " % (item_data, col[item_data]))
    else:
        print("==============Error==============")
        return


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\Desktop\201810\ContactUsOptionsTiles(20181101).xlsx')
    # 获取所有sheet
    sheets = workbook.sheet_names()  # [u'sheet1', u'sheet2']
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


def method_name():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\Desktop\201810\ContactUsOptionsTiles(20181101).xlsx')
    # 获取所有sheet
    sheets = workbook.sheet_names()  # [u'sheet1', u'sheet2']
    # for shrrtItem in sheets:
    #     print(shrrtItem)
    # for index in range(4):
    #     sheetItem = workbook.sheet_by_index(index)
    #     print(sheetItem.name, sheetItem.nrows, sheetItem.ncols)
    #     print(sheetItem.row_values(0))
    sheetItem = workbook.sheet_by_index(0)
    row_values = sheetItem.row_values(0)
    for value in row_values:
        print(value)
    print(sheetItem.col_values(2))


if __name__ == '__main__':
    data = pd.read_csv(r'./csv/oow.csv', encoding='utf-8', names=['A'])
    # print(data)
    data['A'].value_counts().to_csv(r"./csv/oow_1.csv")


