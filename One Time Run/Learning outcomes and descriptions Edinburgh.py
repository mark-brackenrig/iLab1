# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 16:59:30 2018

@author: mbrackenrig
"""



import requests
from bs4 import BeautifulSoup
import pandas
import csv
import regex
import os
os.chdir('C:/Users/mbrackenrig/Desktop/University/Sem2_18/iLab')
subject_codes = pandas.read_csv('Subject Data/Edinburgh_Courses.csv', dtype={'Codes': object})

f = csv.writer(open('Subject Data/Edinburgh_Descriptions.csv', 'w'))
f.writerow(['Descriptions', "Learning_outcomes", "subject_code"])




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


for l in range(0,len(subject_codes)):
#Define the URL that we want
    url = "http://www.drps.ed.ac.uk/18-19/dpt/"+str(subject_codes.subject_code[l])
#do the request thingy so we save the page
    page = requests.get(url) 
#create a soupy mess
    soup = BeautifulSoup(page.text, 'html.parser')
    
    
    for header in soup.find_all('td'):
        nextNode = header
        #print(header)
        if "Summary" in header:
            nextNode = nextNode.nextSibling
            #print(nextNode)
            a = strip_tags(str(nextNode))
            
    for header in soup.find_all("ol"):
        nextNode = header
        nextNode = str(nextNode)
        nextNode = str(regex.sub("</li><li>",".  ",nextNode))
        #print(nextNode)
        b= strip_tags(str(nextNode))
            #print(nextNode)
    b = str(b)
    a = str(a)        
    b = b.encode('utf-8').strip()
    a = a.encode('utf-8').strip()
    f.writerow([a,b,subject_codes.course_name[l]])
           

   
exit()