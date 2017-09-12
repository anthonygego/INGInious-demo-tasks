#!/usr/bin/env python

import random

tlist = []

for i in range(0,10):
    tlist.append(random.random())

thelist = tlist*100
random.shuffle(thelist)

@@sets@@

newlist = remove_duplicates(thelist)

if(len(tlist) == len(newlist) and set(tlist)==set(newlist)):
    print "True"
else:
    print "False"