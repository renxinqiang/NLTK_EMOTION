#!/usr/local/bin/python3


import pymysql

import math

import jieba

import re

comment_file = 'comment.py'

connect = pymysql.connect('127.0.0.1', 'root', 'root', 'comment', charset = 'utf8')
cursor = connect.cursor()



id = 0
size = 10000

sql = "SELECT count(1) as num FROM comment"

cursor.execute(sql)
count = cursor.fetchone()[0]

page = math.ceil(count / size)

times = 1
for x in range(1,page+1):
    where = ''
    if id :
        where = " AND id > "+str(id)
    limit = " LIMIT "+str(size)
    sql = "SELECT id,comment FROM comment WHERE 1 " + where + limit
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()

    if x % 5 == 0:
        comment_file = 'comment'+str(times)+'.py'
        times += 1

    print(comment_file)
    with open(comment_file, 'a', encoding="utf-8") as f:
        for res in result:
            comm = res[1]
            if comm is 'None':
                continue
            r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'  # 用户也可以在此进行自定义过滤字符
            comm = re.sub(r1,'',comm)
            jieba_res = jieba.cut(comm)
            if not jieba_res :
                continue
            write_str = ''
            for res in jieba_res:
                write_str += ',' + "'"+res+"'"
            write_str = write_str + '\n'
            f.write(write_str)

    id = result[-1][0]


cursor.close()
connect.close()