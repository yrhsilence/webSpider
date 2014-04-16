# -*- coding: UTF-8 -*-
'''
@ Created on 2012-3-14
@ summary: 创建数据库脚本
@ author: yrhsilence@126.com
'''
import MySQLdb

def insertData(cur,value):
    'insert data' 
    sql = "insert into %s(url) values('%s')" % value
    cur.execute(sql);
    
    
def createDbAndTable(strhost, struid, strpwd, strdb):
    'create database'
    try:
        conn = MySQLdb.connect(host = strhost,user = struid,passwd = strpwd)
    except:
        print "Open failed!"
    #获取操作游标
    cursor = conn.cursor()
    
    #执行SQL语句，创建一个数据库
    sql = "create database if not exists %s" % strdb
    cursor.execute(sql)

    #选择数据库
    conn.select_db(strdb)

    #执行SQL语句，创建一个urlnew数据表
    sql = "create table urlnew(id int not null primary key auto_increment,url text)"
    cursor.execute(sql)
    
    #执行SQL语句，创建一个urlvisited数据表
    sql = "create table urlvisited(id int not null primary key auto_increment,url longtext)"
    cursor.execute(sql)
        
    cursor.close()#关闭连接，释放资源 
    conn.commit() #提交，在数据库中执行
    conn.close()  
        
if __name__ == "__main__":
    host = 'localhost'
    uid = 'root'
    pwd = '123456'
    db = 'WebSpider'
    
    createDbAndTable(host, uid, pwd, db)
    print 'create database ok!'

         
    



