# overseas_recharge_scrapy_celery

海外商品汇总


### celery 启动

>celery -A consumer_in worker --loglevel=info

### 异步消费
>1. 使用redis作为消息中间件
>2. 利用supervisord作为worker的消费管理
