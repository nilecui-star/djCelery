# Celery

![]()![2522678-d369b6a4c4265225](images/2522678-d369b6a4c4265225.png)



https://www.cnblogs.com/pyedu/p/12461819.html

https://www.celerycn.io/

**firewall-cmd --zone=public --add-port=5672/tcp --permanent**

## 使用场景

celery是一个强大的 分布式任务队列的异步处理框架，它可以让任务的执行完全脱离主程序，甚至可以被分配到其他主机上运行。我们通常使用它来实现异步任务（async task）和定时任务（crontab)。

异步任务：将耗时操作任务提交给Celery去异步执行，比如发送短信/邮件、消息推送、音视频处理等等

定时任务：定时执行某件事情，比如每天数据统计



## 特点

Simple(简单)
Celery 使用和维护都非常简单，并且不需要配置文件。

Highly Available（高可用）
woker和client会在网络连接丢失或者失败时，自动进行重试。并且有的brokers 也支持“双主”或者“主／从”的方式实现高可用。

Fast（快速）
单个的Celery进程每分钟可以处理百万级的任务，并且只需要毫秒级的往返延迟（使用 RabbitMQ, librabbitmq, 和优化设置时）

Flexible（灵活）
Celery几乎每个部分都可以扩展使用，自定义池实现、序列化、压缩方案、日志记录、调度器、消费者、生产者、broker传输等等。



异步任务执行命令：

```shell
celery worker ``-``A celery_app_task ``-``l info
```



# error

```shell
/data # docker run -itd --name redis-test -p 6379:6379 redis
/usr/bin/docker-current: Error response from daemon: Conflict. The container name "/redis-test" is already in use by container dfd0b6775993832d3809cc2daea77178da732ecf4c1d5768789b94ceb4084b1e. You have to remove (or rename) that container to be able to reuse that name..
See '/usr/bin/docker-current run --help'.
```

启动celery成功, 调用任务时报错: [2019-03-04 19:13:17,567: ERROR/MainProcess] Received unregistered task of type 'celery_test1.test'.
The message has been ignored and discarded.

Did you remember to import the module containing this task?
Or maybe you're using relative imports?

Please see
http://docs.celeryq.org/en/latest/internals/protocol.html
for more information.

The full contents of the message body was:
b'[[], {}, {"callbacks": null, "errbacks": null, "chain": null, "chord": null}]' (77b)
Traceback (most recent call last):
File "c:\program files (x86)\python37-32\lib\site-packages\celery\worker\consumer\consumer.py", line 558, in on_task_received
strategy = strategies[type_]
KeyError: 'celery_test1.test'

解决方案: 不要将异步任务函数的定义和调用写到同一个文件中 










