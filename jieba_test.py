#!/usr/local/bin/python3

import jieba
import jieba.analyse


str = '买车通用'
jieba.analyse.set_stop_words('stop_words.txt')
jieba.add_word('买车',freq=20000)
jieba.add_word('通用',freq=0)
tags = jieba.analyse.extract_tags(str)
# test1 = jieba.cut(str)

for x in tags:
    print(x)