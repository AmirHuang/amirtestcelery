# _*_ coding: utf-8 _*_
# @time     : 2019/06/15
# @Author   : Amir
# @Site     : 
# @File     : config.py
# @Software : PyCharm

import datetime
from celery.schedules import crontab
from kombu import Exchange, Queue

BROKER_URL = 'redis://localhost:6379/10'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/11'
CELERY_TIMEZONE = 'Asia/Shanghai'

# 队列
CELERY_QUEUES = (
    Queue("default", Exchange("default"), routing_key="default"),
    Queue("appone_add_queue", Exchange("appone_add_queue"), routing_key="appone_add_router"),
    Queue("apptwo_mult_queue", Exchange("apptwo_mult_queue"), routing_key="apptwo_mult_router")
)
# 路由
CELERY_ROUTES = {
    'appone_add': {"queue": "appone_add_queue", "routing_key": "appone_add_router"},
    'apptwo_mult': {"queue": "apptwo_mult_queue", "routing_key": "apptwo_mult_router"}
}

# 定时任务配置如下
CELERYBEAT_SCHEDULE = {
    'beat_task1': {
        'task': 'appthree_comment',
        'schedule': datetime.timedelta(seconds=2),
        'args': (2, 8)
    },
    'beat_task2': {
        'task': 'appthree_comment',
        'schedule': crontab(hour=16, minute=32),
        'args': (4, 5)
    }
}

# 单独对一个任务启动命令 会启动指定queue
# celery -A celery_tasks.main  worker -l info -n workerA.%h -Q appone_add_queue
# celery -A celery_tasks.main  worker -l info -n workerB.%h -Q apptwo_mult_queue

# 当任务没有指定queue 则任务会加入default 队列 beat(定时任务也会加入default队列)
# celery -A celery_tasks.main  worker -l info -n worker -Q celery

# 启动定时任务
# celery beat -A celery_tasks.main -l INFO


# -A 表示 应用目录  这里是celery_tasks.main
# -B 表示 定时任务
# -l 表示日志级别
# -n woker名
# -Q 队列名
# .%h 对应不同主机ip  如果默认localhost，所以可以省略.%h
# CELERY_CONCURRENCY 每个worker的并发子进程数

# 当有定时任务的时候 可以执行如下两条任务
# celery beat -A celery_app -l INFO   # 表示开始定时任务
# celery worker -A tasks -l INFO      # 表示执行任务 当没有定时任务的时候  也是执行这条

# 当有定时任务的时候  也可以执行一条命令
# celery -B -A celery_app worker -l INFO  # 好像window不行

# -B 表示 定时任务
# -A 表示 应用目录 应用app目录？ 当有多个应用的时候呢  这是一个问题
# -l 表示日志级别
