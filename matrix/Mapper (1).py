#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3
import sys
for line in sys.stdin:
   tokens = line.strip().split(',')
   if tokens[0] == 'A':
       for k in range(0, 2):  # assuming output matrix has 2 columns
           print(f"{tokens[1]},{k}\tA,{tokens[2]},{tokens[3]}")
   elif tokens[0] == 'B':
       for i in range(0, 2):  # assuming output matrix has 2 rows
           print(f"{i},{tokens[2]}\tB,{tokens[1]},{tokens[3]}")
           
hadoop fs -put a.csv /input/a.csv
hadoop fs -put b.csv /input/b.csv
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files mapper.py,reducer.py \
-mapper mapper.py \
-reducer reducer.py \
-input /input \
-output /output_matrix
hadoop fs -cat /output_matrix/part-00000            

