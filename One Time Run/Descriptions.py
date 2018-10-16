# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:52:42 2018

@author: mbrackenrig
"""


import requests
from bs4 import BeautifulSoup
import pandas
import csv
import regex
import os
os.chdir('C:/Users/mbrackenrig/Desktop/University/Sem2_18/iLab')
subject_codes = pandas.read_csv('Subject Data/Subjects.csv', dtype={'Codes': object})

f = csv.writer(open('Subject Data/Descriptions.csv', 'w'))
f.writerow(['Descriptions', "subject_code"])


for l in range(0,len(subject_codes)):
#Define the URL that we want
    url = "http://handbook.uts.edu.au/subjects/details/"+str(subject_codes.Codes[l])+".html"
#do the request thingy so we save the page
    page = requests.get(url) 
#create a soupy mess
    soup = BeautifulSoup(page.text, 'html.parser')
    
    if (l/10) == round(l/10):
        print(l/len(subject_codes))
    
    for header in soup.find_all('h3'):
        nextNode = header
        if "Description" in header:
            #print(header)
            nextNode = nextNode.nextSibling
            sub = str(nextNode.nextSibling).split("<h3>")[0]
            sub = str(regex.sub("<p>","",sub))
            sub = str(regex.sub("</p>","",sub))
            sub= str(regex.sub("[�βα≥ →]","",sub))
            sub = sub.encode('utf-8').strip()
            f.writerow([sub,subject_codes.Codes[l]])

            

#Create function to extract the CILOs
    #CILOs = soup.find(class_='ie-images')


#Extract the SLOs and CILOs
    
    #if CILOs is not None:    
     #   CILOs_items = CILOs.find_all('p')

#We have extracted the SLOs and CILOs and want to use this term later. 
#nested if and for statements do the following
   #if the subject description HAS SLOs run the for loop
       #If thre is an empty entry in the SLO table, skip it
           #If there is a weird chracter, regex replace it
               # Write the SLOs to a CSV
               
 #   if CILOs is not None:
  #      for i in CILOs_items:
   #         if str(i.contents)!='[]':
    #                sub= str(regex.sub("[�βα≥ →]","",str(i.contents[0])))
     #               if "this subject" in sub.lower() and "teaching and learning" not in sub.lower():
                      #  f.writerow([sub,subject_codes.Codes[l] ])

#f.close()
exit()
   
