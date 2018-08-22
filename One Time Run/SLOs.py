# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 19:10:03 2018

@author: mbrackenrig
"""

#Lets try to scrape some shizzz

import requests
from bs4 import BeautifulSoup
import pandas
import csv
import regex
subject_codes = pandas.read_csv('Subjects.csv', dtype={'Codes': object})

f = csv.writer(open('SLOs.csv', 'w'))
f.writerow(['SLOs', "subject_code"])


for l in range(0,len(subject_codes)):
#Define the URL that we want
    url = "http://handbook.uts.edu.au/subjects/details/"+str(subject_codes.Codes[l])+".html"
#do the request thingy so we save the page
    page = requests.get(url) 
#create a soupy mess
    soup = BeautifulSoup(page.text, 'html.parser')

#create a function to extract the SLOs
    SLOs = soup.find(class_='SLOTable')

#extract the CILOs
   # CILOs = soup.find(class_='CILOList')

#Extract the SLOs and CILOs
    if SLOs is not None:
        SLO_items = SLOs.find_all('td')
    
   # if CILOs is not None:    
   #     CILOs_items = CILOs.find_all('td')

#We have extracted the SLOs and CILOs and want to use this term later. 
#nested if and for statements do the following
   #if the subject description HAS SLOs run the for loop
       #If thre is an empty entry in the SLO table, skip it
           #If there is a weird chracter, regex replace it
               # Write the SLOs to a CSV
    
    if SLOs is not None:
        for i in SLO_items:
            if str(i.contents)!='[]':
                if len(regex.findall("�",str(i.contents[0])))<1:    
                    sub = str(i.contents[0])
                    f.writerow([sub,subject_codes.Codes[l] ])
                else: 
                    sub= str(regex.sub("�","",str(i.contents[0])))
                    f.writerow([sub,subject_codes.Codes[l] ])

   
exit('SLOs.csv')
