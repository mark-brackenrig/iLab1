# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 12:53:10 2018

@author: mbrackenrig
"""

##Finding Faculties

#Analytics and Data Science

import pandas as pd

faculties = pd.DataFrame({"Name":["Analytics and Data Science",
"Business",
"Communication",
"Creative Intelligence and Innovation",
"Design, Architecture and Building",
"Education",
"Engineering",
"Health",
"Health (GEM)",
"Information Technology",
"International Studies",
"Law",
"Science",
"Transdisciplinary Innovation" ], 
"URL": ["http://www.handbook.uts.edu.au/ads/lists/numerical.html",
        "http://www.handbook.uts.edu.au/bus/lists/numerical.html",
        "http://www.handbook.uts.edu.au/comm/lists/numerical.html",
        "http://www.handbook.uts.edu.au/cii/lists/numerical.html",
        "http://www.handbook.uts.edu.au/dab/lists/numerical.html",
        "http://www.handbook.uts.edu.au/edu/lists/numerical.html",
        "http://www.handbook.uts.edu.au/eng/lists/numerical.html",
        "http://www.handbook.uts.edu.au/health/lists/numerical.html",
        "http://www.handbook.uts.edu.au/health-gem/lists/numerical.html",
        "http://www.handbook.uts.edu.au/it/lists/numerical.html",
        "http://www.handbook.uts.edu.au/intl/lists/numerical.html",
        "http://www.handbook.uts.edu.au/law/lists/numerical.html",
        "http://www.handbook.uts.edu.au/sci/lists/numerical.html",
        "http://www.handbook.uts.edu.au/tdi/lists/numerical.html",
]})


Subject_Faculty = pd.DataFrame(columns = ["subject","faculty"])


import requests
from bs4 import BeautifulSoup

for i in range(0,len(faculties)):
    page = requests.get(faculties.URL[i]) 

    soup = BeautifulSoup(page.text, 'html.parser')

#Look at the class
    list_raw = soup.find(class_='ie-images')

    #print(list_raw)

    subject_lists = list_raw.find_all('a')

    #print(subject_lists)
    for l in subject_lists:
        sub = str(l.contents[0])
        sub = pd.DataFrame({"subject":[sub],"faculty":[faculties.Name[i]] })
        Subject_Faculty = Subject_Faculty.append(sub, ignore_index= True)


#Cleaning
        
Subject_Faculty = Subject_Faculty.loc[Subject_Faculty["subject"]!="Alphabetical list of subjects"]

Subject_Faculty.to_csv("C:/Users/mbrackenrig/Desktop/University/Sem2_18/iLab/Subject Data/subjects_by_faculty.csv")






