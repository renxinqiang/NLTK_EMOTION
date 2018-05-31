#!/usr/local/bin/python3

import jieba  # 导入jieba模块
import re

# jieba.load_userdict("newdict.txt")  # 加载自定义词典
# import jieba.posseg as pseg


def splitSentence(inputFile, outputFile):
    # 把停用词做成字典
    stopwords = {}
    fstop = open('stop_words.txt', 'r')

    for eachWord in fstop:
        stopwords[eachWord.strip()] = eachWord.strip()
    fstop.close()
    fin = open(inputFile, 'r')  # 以读的方式打开文件
    fout = open(outputFile, 'w')  # 以写得方式打开文件
    # jieba.enable_parallel(4)  # 并行分词
    for eachLine in fin:
        line = eachLine.strip()  # 去除每行首尾可能出现的空格，并转为Unicode进行处理
        line1 = re.sub("[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+", "",
                       line)
        wordList = list(jieba.cut(line1))  # 用结巴分词，对每行内容进行分词
        outStr = ''
        for word in wordList:
            if word not in stopwords:
                outStr += word
                outStr += ' '
        fout.write(outStr.strip().encode('utf-8') + '\n')  # 将分词好的结果写入到输出文件
    fin.close()
    fout.close()

splitSentence('emotion_word.txt','emotion_word.py')