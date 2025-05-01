#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3
import sys
for line in sys.stdin:
   name, marks = line.strip().split('\t')
   marks = int(marks)
   if marks >= 90:
       grade = 'A'
   elif marks >= 80:
       grade = 'B'
   elif marks >= 70:
       grade = 'C'
   elif marks >= 60:
       grade = 'D'
   else:
       grade = 'F'
   print(f"{name}\t{grade}")
   
hadoop fs -put students.txt /input/students.txt
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files mapper.py,reducer.py \
-mapper mapper.py \
-reducer reducer.py \
-input /input/students.txt \
-output /output_grades
hadoop fs -cat /output_grades/part-00000

