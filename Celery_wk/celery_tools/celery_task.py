# -*- encoding: utf-8 -*-
'''
@File    :   celery_task
@Create Time    :   2021/01/24 17:18
@Author  :   nilecui
@Version :   1.0
@Contact :   nilecui@qfoxmail.com
@
'''

import celery
import time

backend = 'redis://192.168.28.128:6379/1'
broker = 'redis://192.168.28.128:6379/2'

cel = celery.Celery('test', backend=backend, broker=broker)


@cel.task
def send_email(name):
    print("向%s发送邮件..." % name)
    time.sleep(5)
    print("向%s发送邮件完成" % name)
    return "ok"


@cel.task
def send_msg(name):
    print("向%s发送短信..." % name)
    time.sleep(5)
    print("向%s发送短信" % name)
    return "ok"
