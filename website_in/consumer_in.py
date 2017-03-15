#!/usr/bin/python
#coding=utf-8

'''
使用这种方法引入本地的python virtural env
'''
activate_this = '/Users/pujielan/ENV/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import time
from celery import Celery
import random

def excute_mysql(sql):
    print "insert into mysql : %s" % sql
    secd = random.randint(2, 7)
    time.sleep(secd)
    pass

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def get_input_mysql(record):
    mm = record['get']
    '''
    sql结构: dbname^_^name^_^price^_^url^_^{'other_2', 'other_2'}
    '''
    mmlist = mm.split('^_^')
    dbname = mmlist[0]
    sql_value = ','.join(mmlist[1:])
    sql = "insert into %s value (%s)" % (dbname, sql_value)
    excute_mysql(sql)
    print sql









