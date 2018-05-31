#!/usr/local/bin/python3


import pymysql

import math

comment_file = 'comment.txt'

connect = pymysql.connect('127.0.0.1', 'root', 'root', 'comment', charset = 'utf8')
cursor = connect.cursor()



id = 0
size = 10000

sql = "SELECT count(1) as num FROM comment"

cursor.execute(sql)
count = cursor.fetchone()[0]

page = math.ceil(count / size)

for x in range(1,page+1):
    where = ''
    if id :
        where = " AND id > "+str(id)
    limit = " LIMIT "+str(size)
    sql = "SELECT id,comment FROM comment WHERE 1 " + where + limit
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()

    with open(comment_file, 'a', encoding="utf-8") as f:
        for res in result:
            comm = res[1]+'\n'
            f.write(comm)

    id = result[-1][0]



cursor.close()
connect.close()