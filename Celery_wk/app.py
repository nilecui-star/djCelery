from flask import Flask, request
from celery import Celery

import logging
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='log_new.log',  # 将日志写入log_new.log文件中
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )

app = Flask(__name__)


app.config['CELERY_BROKER_URL'] = "redis://192.168.11.170:6379/1"
app.config['CELERY_RESULT_URL'] = "redis://192.168.11.170:6379/2"


celery = Celery(app.name,broker=app.config['CELERY_BROKER_URL'],result=app.config['CELERY_RESULT_URL'])
celery.conf.update(app.config)

# https://keras.io/zh/backend/

@app.route('/')
def hello_world():
    try:
        app.logger.info('logged in successfully %s',request.args)

        no_thing = []
        i = no_thing[0]  # 这里会报错，因为列表根本是空的

        return 'Hello World!'
    except Exception as e:
        app.logger.info("%s",e)

#docker-flask_celery-redis
if __name__ == '__main__':
    app.run()
