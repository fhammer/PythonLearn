#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from celery import Celery

'''
celery -A celery_learn.pj.celerys worker --loglevel=info
'''
app = Celery('tasks', broker='redis://10.99.205.17:6379/2')


@app.task
def add(x, y):
    print('Params= ', x, y)
    return x + y
