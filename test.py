#!/usr/local/bin/python3

# import nltk

# print(nltk.corpus.gutenberg.fileids())

# print(len(nltk.corpus.gutenberg.words('austen-emma.txt')))

# from nltk.corpus import  webtext
#
# for fileid in webtext.fileids():
#     print(fileid)

# from nltk.corpus import  nps_chat
#
# chatroom = nps_chat.posts('10-19-20s_706posts.xml')
#
# print(chatroom[123])

# from  nltk.corpus import  brown

# print(brown.categories())

# print(brown.words(categories='news'))

# import nltk
#
# cfd = nltk.ConditionalFreqDist(
#     'hobbies'
# )
# genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
# modals = ['can', 'could', 'may', 'might', 'must', 'will']
# cfd.tabulate(conditions=genres, samples=modals)
#
# print(cfd)

# from nltk.corpus import reuters
#
# print(reuters.categories())

# print(reuters.fileids(['barley','corn']))

# from nltk.corpus import  inaugural

# print(inaugural.fileids())

# cfd = nltk.ConditionalFreqDist(
#     (target,file[:4])
# )
#
# cfd.plot()
#
# print(cfd)

# import nltk
#
# from nltk.corpus import brown
#
# cfd=nltk.ConditionalFreqDist(
# (genre,word)
# for genre in brown.categories()
# for word in brown.words(categories=genre)
# )
# genres=['news','religion','hobbies','science_fiction','romance','humor']
# modals=['can','could','may','might','must','will']
# print (cfd.tabulate(conditions=genres,samples=modals))


# import  nltk
#
# from nltk.corpus import inaugural
# inaugural.fileids()
#
# file = [fileid[:4] for fileid in inaugural.fileids()]
# print(file)
# exit()
# cfd = nltk.ConditionalFreqDist(
#     (target, file[:4])
#     for fileid in inaugural.fileids()
#     for w in inaugural.words(fileid)
#     for target in ['america','citizen']
#     if w.lower().startswith(target)
# )
#
# cfd.plot()

# list = ['Fantastic','!'
# ,'乔布斯','最大','的','成就','之一','，','就是','把','iPhone4','和','iPhone4s','，','打','造成','了','当时','身份','和','档次','的','象征','。','很','显然','，','华为','也','在','模仿','这个','，','华为','mate',' ','RS','，','没','见','什么','质','的','东西','，','当然','，','为','虚荣','买单','的','大','把','的','人','在']


# s = '小米有什么  除了硬件  其它都是用的廉价比如说音质 屏幕 相 机的传感器等一份价钱一分货贵有贵的道理用了对比就知道',\
#
# print(s.replace(' ',''))


level = {'Lv.1':'37480','None':'29515','Lv.2':'9464','Lv.3':'8050','Lv.4':'5436','Lv.5':'2368','Lv.6':'562','Lv.7':'244','Lv.8':'72','Lv.9':'48','Lv.10':'33','Lv.12':'14','Lv.11':'14','Lv.13':'6','Lv.14':'3','Lv.15':'1'}

keys = list(level.keys())
values = list(level.values())
print(values)
