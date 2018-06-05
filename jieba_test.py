#!/usr/local/bin/python3

import jieba
import jieba.analyse


str = '垃 圾 中的 垃圾'
jieba.analyse.set_stop_words('stop_words.txt')
tags = jieba.analyse.extract_tags(str)
# test1 = jieba.cut(str)

for x in tags:
    print(x)