# -*- encoding: utf-8 -*-
"""
@File    :   produce_task
@Create Time    :   2021/01/24 20:20
@Author  :   nilecui
@Version :   1.0
@Contact :   nilecui@qfoxmail.com
@
"""
import time
# from celery_tasks.celery import cel
from .celery import cel


@cel.task
def send_email(name):
    print("向%s发送邮件..." % name)
    time.sleep(5)
    print("向%s发送邮件完成" % name)
    return "ok"
