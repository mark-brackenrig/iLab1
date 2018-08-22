# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 19:37:42 2018

@author: mbrackenrig
"""


import requests
from bs4 import BeautifulSoup
#Get a list of all of the subjects
url = "http://www.handbook.uts.edu.au/subjects/numerical.html"

page = requests.get(url) 

#Create the parser
soup = BeautifulSoup(page.text, 'html.parser')

#Look at the class
list_raw = soup.find(class_='ie-images')

print(list_raw)

subject_lists = list_raw.find_all('a')

print(subject_lists)

import csv

f = csv.writer(open('Subjects.csv', 'w'))
f.writerow(['Link'])

for i in subject_lists:
    sub = str(i.contents[0])
    f.writerow([sub])


exit('Subjects.csv')





