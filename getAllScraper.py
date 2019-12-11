#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:43:16 2019

@author: Taran
"""

import requests 
from bs4 import BeautifulSoup
import urllib.request
import os


###Change this URL
#http://dl.booktolearn.com/ebooks2/science/mathematics/
#http://dl.booktolearn.com/emagazines2/science/
url = "http://dl.booktolearn.com/emagazines2/science/"
  
htmlData=urllib.request.urlopen(url)

soup= BeautifulSoup(htmlData,from_encoding=htmlData.info().get_param('charset'))

myLinks=[]

for link in soup.find_all('a',href=True):
    myLinks.append(link['href'])


#This shows all the books on that page
for i, val in enumerate(myLinks):
    if 'emagazines2' in url.split('/'):
        myName=val
    else:
        myName='_'.join(val.split('_')[1:])
    print (i, "--",myName)
    
# DFunction to Save Specific book
  
def savePDF(num,myLinks):
    fileUrl= url+myLinks[num]

    r = requests.get(fileUrl, stream = True) 

    #this is to remove extrastuff from name, might give some errors
    
    if 'emagazines2' in url.split('/'):
        myName='_'.join(myLinks[num].split('_')[:-1])+'.pdf'
    else:
        myName='_'.join(val.split('_')[1:])
    
    #creating folder name with the subject name
    myPath='./'+url.split('/')[-2]+'/'+myName
    os.makedirs(os.path.dirname(myPath), exist_ok=True)
    
    with open(myPath,"wb") as pdf: 
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: 
                pdf.write(chunk) 

#change num      
savePDF(num=9,myLinks=myLinks)    


#for all books
for i in range(1,len(myLinks)):
    savePDF(num=i,myLinks=myLinks)   
 
    
 
#user defined indexes
myNums = [84,85]             

for i in myNums:
    savePDF(num=i,myLinks=myLinks)                
             