# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:17:15 2018

@author: 1602366
"""

import requests as ur
from bs4 import BeautifulSoup as bs
page=ur.get("https://www.dropbox.com/s/qw66p1gxnzfziyt/Chatterbot11.zip?file_subpath=%2FChatterbot11%2Fchatterbot11.cpp")
print(page.text)
print(page.status_code)
#soup=bs(page.content,'html.parser')
#print(soup.find_all(class_="ui_qtext_rendered_qtext"))
#dat=data.split()
#flag=0
#question=[]
#for i in data:
#    question.append(i.get_text())
#count=1
#for j in question:
#    print(count)
#    print(j+"\n")
#    count+=1;