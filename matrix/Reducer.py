#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3
import sys
from collections import defaultdict
current_key = None
A_vals = defaultdict(float)
B_vals = defaultdict(float)
for line in sys.stdin:
   key, value = line.strip().split('\t')
   matrix, index, val = value.split(',')
   if current_key and current_key != key:
       result = sum(A_vals[k] * B_vals[k] for k in A_vals if k in B_vals)
       print(f"{current_key}\t{result}")
       A_vals.clear()
       B_vals.clear()
   current_key = key
   if matrix == 'A':
       A_vals[index] = float(val)
   else:
       B_vals[index] = float(val)
if current_key:
   result = sum(A_vals[k] * B_vals[k] for k in A_vals if k in B_vals)
   print(f"{current_key}\t{result}")

