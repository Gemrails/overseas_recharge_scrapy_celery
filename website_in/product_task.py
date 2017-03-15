#!/usr/bin/python
#coding=utf-8

'''
使用这种方法引入本地的python virtural env
'''
activate_this = '/Users/pujielan/ENV/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from gevent import monkey
monkey.patch_all()
import gevent
from consumer_in import get_input_mysql
import time
import random

def _time_wait_random(func):
    def decorate(*args, **kw):
        secd = random.randint(3, 7)
        time.sleep(secd)
        print "worker wait time is %d" % secd
        return func(*args, **kw)
    return decorate

@_time_wait_random
def _product(record):
    get_input_mysql.delay(dict(get=record))


if __name__ == '__main__':
    gevent_list = []
    for mm in xrange(10):
        gevent_list.append(gevent.spawn(_product, str(mm)))

    gevent.joinall(gevent_list)

