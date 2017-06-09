#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector


def query_all():
    conn = mysql.connector.connect(user='root', password='root', database='jdbc')
    cursor = conn.cursor()
    cursor.execute("select * from py_user")
    values = cursor.fetchall()
    for value in values:
        print(value)


def create_table():
    conn = mysql.connector.connect(user='root', password='root', database='jdbc')
    cursor = conn.cursor()
    cursor.execute('create table py_user(id VARCHAR(20) PRIMARY KEY ,name VARCHAR(20))')
    cursor.execute('insert into py_user(id,name) values(%s,%s)', ['1', 'hammer'])
    print(cursor.rowcount)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    create_table()
    query_all()
