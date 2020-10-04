#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

# process stdin line
for line in sys.stdin:
    # split line into params
    words = [x.strip() for x in line.split(",")]  # found in google, have no idea how it works
    result = '%s\t%s' % (words[2], words[4])
    print(result)

