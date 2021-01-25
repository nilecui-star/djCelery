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
from .celery import cel


@cel.task
def send_msg(name):
    print("向%s发送短信..." % name)
    time.sleep(5)
    print("向%s发送短信" % name)
    return "ok"
