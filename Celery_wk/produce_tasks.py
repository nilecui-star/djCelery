# -*- encoding: utf-8 -*-
"""
@File    :   produce_task
@Create Time    :   2021/01/24 20:20
@Author  :   nilecui
@Version :   1.0
@Contact :   nilecui@qfoxmail.com
@
"""

from celery_tasks.task01 import send_email
from celery_tasks.task02 import send_msg

res = send_email.delay('1111111111')
print(res.id)

res = send_msg.delay('22222222222')
print(res.id)


