# _*_ coding: utf-8 _*_
# @time     : 2019/06/15
# @Author   : Amir
# @Site     : 
# @File     : main.py
# @Software : PyCharm


from celery import Celery

import os

# 为celery使用django配置文件进行设置
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'amirtestcelery.settings'
# 创建celery应用
app = Celery('amirtestcelery')
# 导入celery配置文件
app.config_from_object('celery_tasks.config')
# 自动注册celery任务，需要启动哪个模块下，则加入列表中
app.autodiscover_tasks(['celery_tasks.appone', 'celery_tasks.apptwo'])

# 启动ｃｅｌｅｒｙ应用
#  celery -A celery_tasks.main worker -l info
