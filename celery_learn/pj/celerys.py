#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from celery import Celery

app = Celery('pj', broker='redis://10.99.205.17:6379/3', backend='redis://10.99.205.17:6379/4', include=['pj.tasks'])

app.config_from_object('pj.config')

if __name__ == '__main__':
    app.start()
