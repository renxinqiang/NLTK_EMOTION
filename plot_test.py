#!/usr/local/bin/python3

import nltk
#
# with open('jb.py','r') as f:
#     content = f.read()
import comment1
import comment2
import comment3
import comment4
import comment5
import comment6
import comment7
import comment8
import comment9
import comment10
import comment11
import comment12
import comment13
import comment14
import comment15
import comment16
import comment17
import comment18
import comment19
import comment20
import comment21


# print(jb.ci)
# exit()
content = comment1.ci + comment2.ci + comment3.ci + \
comment4.ci + comment5.ci + comment6.ci + \
comment7.ci + comment8.ci + comment9.ci + \
comment10.ci + comment11.ci + comment12.ci + \
comment13.ci + comment14.ci + comment15.ci + \
comment16.ci + comment17.ci + comment18.ci + \
comment19.ci + comment20.ci + comment21.ci

cfd = nltk.FreqDist(content)
cfd.tabulate(50)
cfd.plot(50)

