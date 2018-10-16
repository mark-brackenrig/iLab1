# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 16:03:17 2018

@author: mbrackenrig
"""



import requests
from bs4 import BeautifulSoup
import pandas
import csv
import regex
import os
os.chdir('C:/Users/mbrackenrig/Desktop/University/Sem2_18/iLab')




f = csv.writer(open('Subject Data/Edinburgh_Courses.csv', 'w'))
f.writerow(['course_name', "subject_code"])


#Define the URL that we want
url = "http://www.drps.ed.ac.uk/18-19/dpt/cx_sb_infr.htm"
#do the request thingy so we save the page
page = requests.get(url) 
#create a soupy mess
soup = BeautifulSoup(page.text, 'html.parser')
 

from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()   
    
for header in soup.find_all('a'):
   if "infr" in str(header) or "elee" in str(header) or "desi" in str(header):
       if "not_delivered" not in str(header):
           Node = str(header)
           names = strip_tags(Node)
           header = header.get('href')
           print(header)
           f.writerow([names,header])           

exit()


           