# -*- coding: UTF-8 -*-
'''
@ Created on 2012-3-14
@ 创建数据库代码
@ author: yrhsilence@126.com
'''
import MySQLdb

def insertData(cur,value):
    'insert data' 
    sql = "insert into %s(id,url) values(%d,'%s')" % value
    cur.execute(sql);
    
    
def createdb(strhost,struid,strpwd,strdb):
    'create database'
    #conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '123456')
    conn = MySQLdb.connect(host = strhost,user = struid,passwd = strpwd)
    #获取操作游标
    cursor = conn.cursor()
    
    #执行SQL语句，创建一个数据库
    sql = "create database if not exists %s" % strdb
    cursor.execute(sql)

    #选择数据库
    conn.select_db(strdb)

    #执行SQL语句，创建一个urladdre数据表
    sql = "create table urladdre(id int not null primary key auto_increment,url text)"
    cursor.execute(sql)
     
    #插入数据
    value = ("urladdre",1,"www.baidu.com")
    insertData(cursor,value)
    
    #执行SQL语句，创建一个webtest数据表
    sql = "create table webtest(id int not null primary key auto_increment,url longtext)"
    cursor.execute(sql)
    
    #插入数据
    value = ("webtest",1,"my name is yuronghua")
    insertData(cursor,value)
    
    cursor.close()#关闭连接，释放资源 
    conn.commit() #提交，在数据库中执行
    conn.close()

if __name__ == "__main__":
    host = 'localhost'
    uid = 'root'
    pwd = '123456'
    db = 'mydb'
    createdb(host,uid,pwd,db)
    print 'create database ok!'

         
    




