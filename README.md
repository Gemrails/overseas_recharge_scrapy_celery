# overseas_recharge_scrapy_celery

>海外商品汇总



### celery 启动

* celery -A consumer_in worker --loglevel=info

### 异步消费
* 使用redis作为消息中间件
* 利用supervisord作为worker的消费管理


  [program:consumer_celery]
  command=/usr/bin/celery worker -A consumer_in
  directory=/xxx/xxx
  stdout_logfile=/data/logs/celery.log
  autostart=true
  autorestart=true
  redirect_stderr=true
  stopsignal=QUIT`
