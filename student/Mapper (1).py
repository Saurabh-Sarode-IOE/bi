#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3
 import sys
 for line in sys.stdin:
    line = line.strip()
    if line:
        name, marks = line.split(',')
        print(f"{name}\t{marks}")

