#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
# Read input line by line
for line in sys.stdin:
   line = line.strip()
   words = line.split()
   for word in words:
       print(f'{word}\t1')

