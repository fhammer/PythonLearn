# -*- coding: utf-8 -*-
from datetime import timedelta
from celery.schedules import crontab

# Broker and Backend
BROKER_URL = 'redis://10.99.205.17:6379'  # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://10.99.205.17:6379/0'  # 指定 Backend
CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'
CELERY_IMPORTS = (  # 指定导入的任务模块
    'celery_app.task1',
    'celery_app.task2'
)

# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=30),  # 每 30 秒执行一次
        'args': (5, 8)  # 任务函数参数
    },
    'multiply-at-some-time': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=9, minute=50),  # 每天早上 9 点 50 分执行一次
        'args': (3, 7)  # 任务函数参数
    }
}

'''
celery -A celery_app worker --loglevel=info // -l info
-A指定的是app(即Celery实例)所在的文件模块，我们的app是放在celery_app中，
所以这里是 celery_app；worker表示当前以worker的方式运行，难道还有别的方式？对的，比如运行定时任务就不用指定worker这个关键字; 
-l info表示该worker节点的日志等级是info，和--loglevel=info 一样。
更多关于启动worker的参数(比如-c、-Q等常用的)请使用 celery worker --help 

启动 Celery Worker 进程
celery -A celery_app worker --loglevel=info // -l info

启动 Celery Beat 进程，定时将任务发送到 Broker
celery beat -A celery_app

一个命令启动上面两个进程
celery -B -A celery_app worker --loglevel=info
'''
