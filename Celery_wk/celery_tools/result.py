# -*- encoding: utf-8 -*-
"""
@File    :   produce_task
@Create Time    :   2021/01/24 20:20
@Author  :   nilecui
@Version :   1.0
@Contact :   nilecui@qfoxmail.com
@
"""
from celery.result import AsyncResult
from celery_task import cel

async_result = AsyncResult(id="b18ace8b-7402-4bc8-adbf-7ff51eec1deb")

if async_result.successful():
    result = async_result.get()
    print(result)
elif async_result.failed():
    print("n failed!")
elif async_result.status == "PENDING":
    print("task waiting!")
elif async_result.status == "RETRY":
    print("Exception....")
elif async_result.status == "STARTED:":
    print('task start....')
