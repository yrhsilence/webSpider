#-*-encoding:utf-8-*-

'''
Created on 2012-5-12
@file: function.py
@summary: 一些操作函数的实现
@author: yrhsilence@126.com
'''
from urlparse import urlparse
from os.path import isdir, exists, dirname, splitext
from os import makedirs, unlink, sep
from string import replace

#定制你需要的url
def isurl(url):
    if url[0:7] == "http://":
        return True
    else:
        return False

def urlOnlyOne(url):
    pass

#根据url建立文件位置
def filename(url, deffile='index.htm'):
    parsedurl = urlparse(url, 'http:', 0)  # parse path
    path = parsedurl[1] + parsedurl[2]
    ext = splitext(path)
    if ext[1] == '':
        if path[-1] == '/':
            path += deffile
        else:
            path += '/' + deffile
    ldir = dirname(path)    # local directory
    if sep != '/':        # os-indep. path separator
        ldir = replace(ldir, ',', sep)
    if not isdir(ldir):      # create archive dir if nec.
        if exists(ldir): unlink(ldir)
        makedirs(ldir)
    return path
