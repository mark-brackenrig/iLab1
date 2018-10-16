# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:29:16 2018

@author: mbrackenrig
"""

import spacy

nlp = spacy.load('en_core_web_lg')

import os

os.chdir('C:/Users/mbrackenrig/Desktop/University/Sem2_18/iLab/iLab_Repository')

from setup import Descriptions, Edinburgh_Descriptions
Edinburgh_Descriptions = Edinburgh_Descriptions.drop_duplicates()

Descriptions = Descriptions.drop_duplicates()
#Experiment 1 - Using spacy, link degrees in Edinburgh to course Descriptions


import pandas
import numpy

columns = ["Edinburgh_subject", "similarity", "UTS_code"]

Results = pandas.DataFrame(columns = columns)


i=0    
for l in Edinburgh_Descriptions.Descriptions:

    tests = pandas.DataFrame({"similarity": numpy.zeros(len(Descriptions)), "UTS_code":Descriptions.subject_code})    
    Edin = nlp(l)

    
    tests.similarity = pandas.Series([Edin.similarity(nlp(i)) for i in Descriptions.Descriptions])
#    for i in range(0, len(Descriptions)):
 #       Desc = nlp(Descriptions.Descriptions[i])
  #      tests.similarity[i] = Edin.similarity(Desc)    
        
    sorts = tests.nlargest(5,'similarity')
    sorts['Edinburgh_subject']= Edinburgh_Descriptions.loc[Edinburgh_Descriptions['Descriptions'] == l, 'subject_code']
    Results = Results.append(sorts, ignore_index = True)
    i=i+1
    print(round(i*100/len(Edinburgh_Descriptions)))
    

Results.to_csv("C:/Users/mbrackenrig/Desktop/University/Sem2_18/iLab/iLab_Repository/Experiments/Results/Experiment_1_Results.csv")
#Top 5 subjects in UTS
    #Introduction to Programming for Mathematics
    #Computer-aided Mechanical Design
    #Architectural Design Capstone Project: Integration
    #Advanced Architectural Construction
    #Applied Electronics and Interfacing
print("First Experiment Complete")
    #Architecture is a bit weird but first two are okay.
import gc    
del(Descriptions)
del(sorts)
del(Results)
del(tests)
del(columns)
gc.collect()

from setup import SLOs

#Concatenate SLOs by subject Code
 
codes= numpy.unique(SLOs.subject_code)

columns = ["Edinburgh_subject", "similarity", "UTS_code"]

Results = pandas.DataFrame(columns = columns)
i = 0
for l in Edinburgh_Descriptions.Learning_outcomes:
    Edin = nlp(l)
    tests = pandas.DataFrame({"similarity": numpy.zeros(len(SLOs)), "UTS_code":SLOs.subject_code})    
    
    
    tests.similarity = pandas.Series([Edin.similarity(nlp(i)) for i in SLOs.SLOs])
#   
    #for i in range(0, len(SLOs)):
     #   Desc = nlp(SLOs.SLOs[i])
      #  tests.similarity[i] = Edin.similarity(Desc)
       
    groups = tests.groupby('UTS_code').mean()
    sorts = groups.nlargest(5,'similarity')
    sorts['UTS_code'] = sorts.index

    sorts['Edinburgh_subject']= Edinburgh_Descriptions.loc[Edinburgh_Descriptions['Descriptions'] == l, 'subject_code']
    Results = Results.append(sorts, ignore_index = True)
    i=i+1
    print(round(i*100/len(Edinburgh_Descriptions)))

Results.to_csv("C:/Users/mbrackenrig/Desktop/University/Sem2_18/iLab/iLab_Repository/Experiments/Results/Experiment_1_Results_SLOs.csv")





