# -*- coding: UTF-8 -*-
'''
Created on 2012-5-8
@file: MyParser.py
@summary: 解析HTML，提取其中的URL
@author: yrhsilence@126.com    
'''

import urllib2
from urllib import urlretrieve
from sgmllib import SGMLParser
from function import filename

#继承SGMLParser类，实现HTML的解析
class MyParser(SGMLParser):
    def reset(self):
        self.urls = []
        self.datas = []
        SGMLParser.reset(self)
    
    def parse(self, data):
        self.feed(data)
        self.close()
        
    def start_a(self, attr):
        for name, value in attr:
            if name == "href":
                self.urls.append(value)
                
    def handle_data(self, data):
        self.datas.append(data) 

#写出一个页面中的所有链接
def getURL(startURL):
    try:
        sock=urllib2.urlopen(startURL)
    except:
        return []
    try:
        filepath = filename(startURL)
        urlretrieve(startURL, filepath)
        getdata=sock.read()
        sock.close()
    except:   
        print "urlretrieve error!"     
    try:
        parser=MyParser()
        parser.parse(getdata)
        #parser.parse(startURL)
        parser.close()
    except:
        print "Parser error!"
        
    return parser.urls
    