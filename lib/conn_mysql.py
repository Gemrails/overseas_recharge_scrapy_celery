#!/usr/bin/python
#coding=utf-8

'''
mysql 调用封装类
'''
'''
import MySQLdb

class Mmysql():
    def __init__(self, dbn):

        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.passwd = 'root'
        self.db = dbn

    def



        conn= MySQLdb.connect(
            self.host,
            self.port,
            self.user,
            self.passwd,
            self.db,
            )
        self.cur = conn.cursor()

'''

from read_ini import Config as CF
import MySQLdb
from debug_print import debug_print as dprint

class MySQLHelper(object):
    def __init__(self, charset="utf8"):
        self.cf = CF()
        self.host = self.cf.getvalue('mysql_cnf', 'host')
        self.user = self.cf.getvalue('mysql_cnf', 'user')
        self.password = self.cf.getvalue('mysql_cnf', 'passwd')
        self.charset = charset
        self.port = self.cf.getvalue('mysql_cnf', 'port')
        try:
            self.conn = MySQLdb.connect(host=self.host,user=self.user,passwd=self.password,port=int(self.port))
            self.conn.set_character_set(self.charset)
            self.cur = self.conn.cursor()
            dprint("init OK.")
        except MySQLdb.Error as e:
            errmsg = "Mysql Error %d: %s" % (e.args[0], e.args[1])
            dprint(errmsg)

    def selectDb(self,db):
        try:
            self.conn.select_db(db)
        except MySQLdb.Error as e:
            errmsg = "Mysql Error %d: %s" % (e.args[0], e.args[1])
            dprint(errmsg)

    def query(self,sql):
        try:
            n = self.cur.execute(sql)
            return n
        except MySQLdb.Error as e:
            errmsg = "Mysql Error:%s\nSQL:%s" %(e,sql)
            dprint(errmsg)

    def queryRow(self,sql):
        self.query(sql)
        result = self.cur.fetchone()
        dprint(result)
        return result

    def queryAll(self,sql):
        self.query(sql)
        result = self.cur.fetchall()
        desc = self.cur.description
        d = []
        for inv in result:
             _d = {}
             for i in range(0,len(inv)):
                 _d[desc[i][0]] = str(inv[i])
             d.append(_d)
        return d

    def insert(self,p_table_name,p_data=None,info=''):
        key   = p_data.keys()
        value = p_data.values()
        real_sql = "INSERT INTO " + p_table_name + "(`key`, `value`) " + "VALUES " + \
                   "(" + '"'+ key[0] +'"' + "," + '"' + value[0] + '"' + info + ")"
        #self.query("set names 'utf8'")
        dprint(real_sql)
        return self.query(real_sql)


    def getLastInsertId(self):
        return self.cur.lastrowid

    def rowcount(self):
        return self.cur.rowcount

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
