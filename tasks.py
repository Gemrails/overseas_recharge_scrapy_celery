#!/usr/bin/python
#coding=utf-8

activate_this = '/Users/pujielan/ENV/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from celery import Celery
import time

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')
