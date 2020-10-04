#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

current_country = None
current_sum = 0.0
country = None

for line in sys.stdin:
    line = line.strip()
    country, payout = line.split("\t", 1)

    # convert payout to float
    try:
        payout = float(payout)
    except ValueError:
        continue

    if current_country == country:
        current_sum += payout
    else:  # countries don't match, it means we switch to a new country in the list
        if current_country:
            print("%s\t%s" % (current_country, current_sum))
        current_country = country
        current_sum = payout

# output the last word
if current_country == country:
    print("%s\t%s" % (current_country, current_sum))

