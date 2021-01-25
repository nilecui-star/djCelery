[uwsgi]
# 启动主进程，来管理其他进程
master = true
# 地址和端口号
http = :8001 
# app.py路径
wsgi-file =  app.py  
# uwsgi指定的是application，而flask中是app
callable = app
# 开启的进程数量
processes = 2
# 运行线程
threads = 8
# 设置用于uwsgi包解析的内部缓存区大小为64k。默认是4k
buffer-size = 32768

uwsgi是一个通用server服务器，支持Python， Ruby等多种语言。uwsgi支持自动伸缩，当空闲超过一定时间，会关闭worker，当请求处理不过来需要排队时，

创建新的worker。

 

# 启用process manager，管理worker进程，worker进程都是这个master进程的子进程
master = true

启动 uwsgi

uwsgi uwsgi.ini
4、停止 uwsgi

pkill -f -9 uwsgi

 

# wsgi文件

wsgi-file = wsgi.py

 

# 该对象就是一个wsgi接口，如Flask中的app
callable = WSGIHandler

 

# 在app加载前切换到当前目录
chdir = /web/www/mysite

 

# 监控项目的py文件的mtime来触发重载 (只在开发时使用)，py-autoreload表示多长时间检测一次，单位秒
py-autoreload=1

 

# 在每个worker而不是master中加载应用。默认为false，表示先加载应用，再fork出worker，这样做可以让work尽量共用内存，只有当写时才copy

# 由于先加载再fork，但有些东西是不支持fork的，比如socket连接，所以lazy-apps=false时，不要在加载应用时自动创建数据库连接等

lazy-apps=true

 

# 指定监听该机器所有IP的5000端口
http-socket = :5000

 

# 指定unix domain socket文件。只有当你上游服务器如Nginx与uwsgi服务器在一台机器上时才可以使用
socket = /test/myapp.sock

 

 

# 启动2个worker进程
processes = 2

 

# 每个worker进程中创建两个线程
threades = 2

 

# 设置用于uwsgi包解析的内部缓存区大小为64k。默认是4k。
buffer-size = 32768

 

# 使进程在后台运行，并将日志打到指定的日志文件或者udp服务器
daemonize = /var/log/myapp_uwsgi.log

 

# 设置最大日志文件大小
log-maxsize = 5000000

 

# 禁用请求日志记录
disable-logging = true

 

# 当服务器退出的时候自动删除unix socket文件和pid文件。
vacuum = true

 

# 设置socket的监听队列大小（默认：100）
listen = 120

# 指定pid文件
pidfile = /var/run/uwsgi.pid

 

# 这个参数不会影响app内创建线程，只影响wsgi内部的api，默认值为false。可以认为对用户无影响，使用默认值即可。参见 https://github.com/unbit/uwsgi/issues/1141
enable-threads = true

 

# 设置在平滑的重启（直到接收到的请求处理完才重启）一个工作子进程中，等待这个工作结束的最长秒数。这个配置会使在平滑地重启工作子进程中，如果工作进程结束时间超过了8秒就会被强行结束（忽略之前已经接收到的请求而直接结束）
reload-mercy = 8

 

# 为每个工作进程设置请求数的上限。当一个工作进程处理的请求数达到这个值，那么该工作进程就会被回收重用（重启）。你可以使用这个选项来默默地对抗内存泄漏
max-requests = 5000

 

# 通过使用POSIX/UNIX的setrlimit()函数来限制每个uWSGI进程的虚拟内存使用数。这个配置会限制uWSGI的进程占用虚拟内存不超过256M。如果虚拟内存已经达到256M，并继续申请虚拟内存则会使程序报内存错误，本次的http请求将返回500错误。

limit-as = 256

 

# 一个请求花费的时间超过了这个harakiri超时时间，那么这个请求都会被丢弃，并且当前处理这个请求的工作进程会被回收再利用（即重启）
harakiri = 60

https://www.cnblogs.com/oklizz/p/11385847.html
https://blog.csdn.net/weixin_43988672/article/details/102673461