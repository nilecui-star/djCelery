# -*- encoding: utf-8 -*-
"""
@File    :   produce_task
@Create Time    :   2021/01/24 20:20
@Author  :   nilecui
@Version :   1.0
@Contact :   nilecui@qfoxmail.com
@
"""

from celery import Celery
import time

backend = 'redis://192.168.28.128:6379/1'
broker = 'redis://192.168.28.128:6379/2'

cel = Celery('celery_demo',
             backend=backend,
             broker=broker,
             include=['celery_tasks.task01',
                      'celery_tasks.task02'
                      ])

# time
cel.conf.timezone = 'Asia/Shanghai'

#
cel.conf.enable_utc = False
