#!/usr/local/bin/python3

import jieba

str = 'Fantastic!'
test1 = jieba.cut(str)

for x in test1:
    print(x)