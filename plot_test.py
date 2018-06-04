#!/usr/local/bin/python3

import nltk

with open('comment0.pyr') as f:
    content = f.read()

print(content)

cfd = nltk.FreqDist(content)

cfd.tabulate()

