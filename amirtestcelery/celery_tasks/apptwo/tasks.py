# _*_ coding: utf-8 _*_
# @time     : 2019/06/15
# @Author   : Amir
# @Site     : 
# @File     : tasks.py
# @Software : PyCharm


import time
from celery_tasks.main import app


@app.task(name='apptwo_mult')
def mult(x, y):
    print('start apptwo mult function')
    time.sleep(10)
    print('result:', x * y)
    return x * y