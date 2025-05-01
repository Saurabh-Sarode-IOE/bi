#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
current_word = None
current_count = 0
# Input comes from standard input
for line in sys.stdin:
   word, count = line.strip().split('\t')
   try:
       count = int(count)
   except ValueError:
       continue
   if current_word == word:
       current_count += count
   else:
       if current_word:
           print(f'{current_word}\t{current_count}')
       current_word = word
       current_count = count
# Output the last word
if current_word == word:
   print(f'{current_word}\t{current_count}')
   
   
   
# hadoop fs -put input.txt /input
# hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
# -input /input/input.txt \
# -output /output \-mapper mapper.py \
# -reducer reducer.py
# hadoop fs -cat /output/part-00000

