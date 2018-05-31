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

