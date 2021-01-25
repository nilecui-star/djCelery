# -*- encoding: utf-8 -*-
'''
@File    :   produce_task
@Create Time    :   2021/01/24 20:20
@Author  :   nilecui
@Version :   1.0
@Contact :   nilecui@qfoxmail.com
@
'''

from celery_task import send_email, send_msg

result = send_email.delay("yuan")
print(result.id)

result = send_msg.delay("haha")
print(result.id)