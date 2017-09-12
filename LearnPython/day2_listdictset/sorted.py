#!/usr/bin/env python

import random

tlist = []

for i in range(0,10):
    tlist.append(
    {
        "name": ''.join(random.choice('abcde') for _ in range(7)), 
        "price":random.uniform(0,200)
    })

@@sorted@@

print sorted_by_price(tlist) == sorted(tlist, key=lambda k: k["price"])