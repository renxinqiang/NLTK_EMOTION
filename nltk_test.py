#!/usr/local/bin/python3

# from nltk import *
# import matplotlib
#
# matplotlib.use('TkAgg')
#
# with open('comment0.py','r') as f:
#     text1 = f.read()
#
# fdist = FreqDist(text1)
# fdist.plot()
#

# import nltk
# # from nltk.corpus import inaugural
# import matplotlib
#
#
#
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# # print(list(f[:4]for f in inaugural.fileids()))
# # 下面体现American和citizen随时间推移使用情况
# # cfd = nltk.ConditionalFreqDist( \
# #     (target, fileid[:4]) \
# #     for fileid in inaugural.fileids() \
# #     for w in inaugural.words(fileid) \
# #     for target in ['america', 'citizen'] \
# #     if w.lower().startswith(target))
# str = ['乔布斯','最大','的','成就','之一','，','就是','把','iPhone4','和','iPhone4s','，','打','造成','了','当时','身份','和','档次','的','象征','。','很','显然','，','华为','也','在','模仿','这个','，','华为','mate',' ','RS','，','没','见','什么','质','的','东西','，','当然','，','为','虚荣','买单','的','大','把','的','人','在']
#
# list1 = []
# [list1.append(x) for x in range(len(str))]
#
# plt.xlabel('x轴')
#
# plt.ylabel('y轴')
#
# plt.bar(left = str,height =list1,width = 0.35)
#
# plt.show()
# import nltk
# import comment1
# str = ' '
# pi = "'"+str.join(comment1.ci)+"'"
#
# text = nltk.word_tokenize(pi)
# print(nltk.pos_tag(text))


import nltk
import comment1
from nltk.corpus import names
import random

# def gender_features(word): #特征提取器
#     return {'last_letter':word[-1]} #特征集就是最后一个字母

# names = [(name,'male') for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')]
#
# random.shuffle(names)#将序列打乱
# features = [(gender_features(n),g) for (n,g) in names]#返回对应的特征和标签

def set_word(word):
    if 1:
        tup1 = {'last_letter':word},'bad'
    else:
        tup1 = (word,'good')
    return tup1

words = comment1.ci

features = [set_word(n) for (n) in words]


train,test = features[500:],features[:500] #训练集和测试集

classifier = nltk.NaiveBayesClassifier.train(train) #生成分类器

print('Renxinqiang is a',classifier.classify(set_word('Renxinqiang')))#分类

print(nltk.classify.accuracy(classifier,test)) #测试准确度

classifier.show_most_informative_features(5)#得到似然比，检测对于哪些特征有用


