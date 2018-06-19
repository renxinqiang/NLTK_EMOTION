#!/usr/local/bin/python3

# exit('shuijiao')
import pymysql

import math

import jieba.analyse

import re

comment_file = 'comment.py'

connect = pymysql.connect('127.0.0.1', 'root', 'root', 'comment', charset = 'utf8')
cursor = connect.cursor()



id = 0
size = 50000

sql = "SELECT count(1) as num FROM comment"

cursor.execute(sql)
count = cursor.fetchone()[0]

page = math.ceil(count / size)

jieba.analyse.set_stop_words('stop_words.txt')
jieba.add_word('脑子瓦塔',freq=20000)
jieba.add_word('玛吉亚巴库内',freq=20000)
for x in range(1,page+1):
    where = ''
    if id :
        where = " AND id > "+str(id)
    limit = " LIMIT "+str(size)
    sql = "SELECT id,comment FROM comment WHERE 1 " + where + limit
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()

    comment_file = 'comment'+str(x)+'.py'
    print(comment_file)
    with open(comment_file, 'a', encoding="utf-8") as f:
        f.write('ci = ')
        for res in result:
            comm = res[1]
            if comm is 'None':
                continue
            r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~～……]+'  # 用户也可以在此进行自定义过滤字符
            comm = re.sub(r1,'',comm)
            if not comm :
                continue
            jieba_res = jieba.analyse.extract_tags(comm)
            if not jieba_res :
                continue
            write_str = ''
            for row in jieba_res:
                if not row or row is ' ' or row is '  ':
                    continue
                write_str += "'"+row+"'" + ','
            if not write_str:
                continue
            write_str = write_str + '\\\n'
            f.write(write_str)

    id = result[-1][0]


cursor.close()
connect.close()