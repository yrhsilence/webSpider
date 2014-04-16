# -*- coding: UTF-8 -*-
'''
Created on 2012-5-16
@file: Mysql.py
@summary: mysql数据库操作类
@author: root
'''
import MySQLdb

class Mysql():
    conn = ""
    cursor = ""
    
    def __init__(self, host='localhost', usr='root', password='123456', database='test'):
        self.conn = MySQLdb.connect(host = host, user = usr, passwd = password, db = database)
        self.cursor = self.conn.cursor()
        
    def __del__(self):
        self.cursor.close()
        self.conn.close()
    
    def query(self, sql):
        return self.cursor.execute(sql)

    def commit(self):
        self.conn.commit()
        
    def insertOneUrl(self, value):
        sql = "insert into %s(url) values('%s')" % value
        self.cursor.execute(sql)
    
    def delUrl(self, tableName, delNum):
        sql = "delete from %s where id <= %d" % (tableName, delNum)
        count = self.cursor.execute(sql)
        self.conn.commit()
        return count
        
        
    def getUrl(self, tableName, urlNum):
        sql = "select url from %s" % tableName
        count = self.cursor.execute(sql)
        if count <= urlNum:
            urlNum = count
        urllist = self.cursor.fetchmany(urlNum)
        #num = self.delUrl(tableName, self.delNum)
        self.conn.commit()
        return urllist
    
    
    def putUrl(self, tableName, urlSet):
        for url in urlSet:
            sql = "insert into %s(url) values('%s')" % (tableName, url)
            self.cursor.execute(sql)
        self.conn.commit() 