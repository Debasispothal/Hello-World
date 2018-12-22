# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:04:01 2018

@author: 1602366
"""

import pandas as pa
count1=[]
set1=pa.read_csv("C:\\Users\\nEW u\\Desktop\\web scraping\\topic_dataset.csv",engine="python")
set2=pa.read_csv("C:\\Users\\nEW u\\Desktop\\web scraping\\500_questions.csv",engine="python")
for _ in range(0,500):
    count1.append(0)
set2['coun']=count1
top=set1['topic']
sub=set1['subject']
que=set2['question']
#print(set2.columns)

for i in top:
    ind=-1
    for j in set2['question']:
        ind+=1
        for k in j.split():
            if i==k.lower():
               set2.loc[ind,'coun']+=1
xc=list(set2['coun'])              
xc.sort()
count=1
l=[]
for i in range(xc[-1],1,-1):
    ind=-1
    for j in set2['coun']:
        ind+=1
        if j==i:
            print("("+str(count)+")"+set2.loc[ind,'question']+"\n")
            l.append(set2.loc[ind,'question'])
            count+=1
            if count>20:
                break
        if count>20:
            break;
file=pa.DataFrame(l)
#file.to_csv("C:\\Users\\nEW u\\Desktop\\web scraping\\final1.csv")
      
#    res=[]
#    for j in que:
#        for k in j.split():
#            if i==k:
#                res.append(j)
#                break
#            
#    print("\nthe question for "+i+'------------------------------\n')
#    count=1
#    for l in res:
#        print("("+str(count)+")"+" "+l)
#        count+=1        