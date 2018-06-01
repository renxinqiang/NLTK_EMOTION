#!/usr/local/bin/python3

from nltk import *
# txt = Text(text1)
# for t in txt:
#     print(t)
text1 = ['whale','fsadf','whale','whale']
text12 = text1 * 1040000
fdist = FreqDist(text12)
# fdist.plot(TopK,cumulative=True)
print(fdist['whale'])