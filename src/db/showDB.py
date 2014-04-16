# -*- coding: UTF-8 -*-
'''
@ Created on 2012-3-15
@ 显示数据库中的内容
@ author: yrhsilence@126.com
'''
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='mydb')
cursor = conn.cursor()

table = 'urladdre'
sql = 'select * from %s' % table
count = cursor.execute(sql)

#result = cursor.fetchone()  #获得一条记录
#results = cursor.fetchmany(5)  #获得五条记录
 
results = cursor.fetchall() #获得所有结果
for each in results:
    print "id:%d url:%s" % each

cursor.close() 
conn.close()
