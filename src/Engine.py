# -*- coding: UTF-8 -*-
'''
Created on 2012-5-11
@file: Engine.py
@summary: 控制器
@author: yrhsilence@126.com
'''

import threadpool
import datetime
import MyParser
import threading 
import function
from bloomfilter import BloomFilter
from Queue import Queue
from Mysql import Mysql
from DbOperate import createDbAndTable

e = BloomFilter(m = 1000000, k = 4)
urlResult = Queue()  #结果url队列
mylock = threading.RLock() 
count = 0

def urlIsOnly(url):
    if url in e:
        return False
    else:
        e.add(url)
        return True
        
def writeFile(request,result):
    for item in result:
        
        if function.isurl(item) and urlIsOnly(item):
            #print item
            urlResult.put(item)
        
def usingThreadpool(num_thread, urlRequst):         
    start = datetime.datetime.now()  
    main = threadpool.ThreadPool(num_thread)   
    
    if 0 == len(urlRequst):
        print "urlRequst is empty!"
        return
    for url in urlRequst:
        try :
            req = threadpool.WorkRequest(MyParser.getURL, args=[url[0]], kwds={}, callback=writeFile)
            main.putRequest(req)
        except Exception ,e:
            print e
         
    while True:
        try:
            main.poll()
        except threadpool.NoResultsPending:
            print "no pending results"
            break
        except Exception ,e:
            print e
            
    end = datetime.datetime.now()   
    print "Start at :\t" , start
    print "End at :\t" , end
    print "Total Cost :\t" , end - start
    main.stop()
 
def InitDb(host, uid, pwd, db, table, inputfile):
    createDbAndTable(host, uid, pwd, db)
    #连接数据库
    mydb = Mysql(database = db) 
    
    #初始化搜索列表
    urlfile = open(inputfile, "r") 
    mydb.putUrl(table, urlfile)
    
    
def main(): 
    #在mysql中创建数据库
    host = 'localhost'
    uid = 'root'
    pwd = '123456'
    db = 'WebSpider'
    table = 'urlnew'
    inputfile = "input.txt"
    InitDb(host, uid, pwd, db, table, inputfile)
    
    delNum = 0  #数据库中被删除的url个数
    while True:
        mydb = Mysql(database = db)
        urlRequest = mydb.getUrl(table, 20)       
        length = len(urlRequest)
        if 0 == len(urlRequest):
            print "URL is over"
            break
        
        delNum = delNum + length
        mydb.delUrl(table, delNum)
        
        usingThreadpool(10, urlRequest)
        
        mylock.acquire()
        while True:
            if 0 == urlResult.qsize():
                #print "urlResult is Empty!"
                break
            url = urlResult.get()
            value = ("urlnew", url)
            mydb.insertOneUrl(value)
        mydb.commit()
        mylock.release()

if __name__ == "__main__":
    main()
    
