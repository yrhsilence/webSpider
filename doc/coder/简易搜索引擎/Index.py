import string
import sys
import re
import MySQLdb

conn = MySQLdb.connect(host = 'localhost',
                       user = 'root',
                       passwd = '123456',
                       db = 'yrh')

cursor = conn.cursor()
cursor.execute("truncate table search")

def makeIndex(myurl, link):
    href = link
    page = myurl
    f = open(page, "rb") 

    wordcount = 0
    words = {}

    for line in f.readlins():
        line = string.strip( line )
        for word in re.split("[" + string.whitespace
                             +string.punctuation + "]", line):
            word = string.lower(word)
            if re.match("^[" + string.lowercase + "]+$", word):
                wordcount += 1
                if words.has_key(word):
                    words[word] += 1
                else:
                    words[word] = 1

    sorted_word_list = words.keys()
    sorted_word_list.sort()

    for word in sorted_word_list:
        cursor.execute('''insert into search(word,occurrence,url,link)
                       values(%s,%s,%s,%s)''',(word,words[word],page,href))

    f.close


makeIndex("mypage1.html","a href = \"www.baidu.com\">my page 1")
makeIndex("mypage1.htm2","a href = \"www.sina.com\">my page 2")
