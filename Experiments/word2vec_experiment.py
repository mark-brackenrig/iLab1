# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 06:17:52 2018

@author: Administrator
"""

import os 
os.chdir("C:/Users/Administrator/Documents/Word2Vec Model")
os.getcwd()


from gensim.models import Word2Vec

model = Word2Vec.load("word2vec.model")

os.chdir("C:/Users/Administrator/Documents")

import pandas

Descriptions = pandas.read_csv("Subject Data/Descriptions.csv")

Edinburgh_Descriptions = pandas.read_csv("Subject Data/Edinburgh_Descriptions.csv")

Edinburgh_Descriptions = Edinburgh_Descriptions.drop_duplicates()

Descriptions = Descriptions.drop_duplicates()

import numpy

columns = ["Edinburgh_subject", "similarity", "UTS_code"]

Results = pandas.DataFrame(columns = columns)


i=0    
for l in Edinburgh_Descriptions.Descriptions:

      
    Edin = l.lower()
    Edin = Edin.replace('[^\w\s]','')
    Edin = Edin.replace('\d+','').split()
    
    tests = pandas.DataFrame({"similarity": pandas.Series([model.wv.wmdistance(Edin,i.lower().replace('[^\w\s]','').replace('\d+','').split() )for i in Descriptions.Descriptions]), "UTS_code":Descriptions.subject_code, "Edinburgh_subject":pandas.concat([Edinburgh_Descriptions.loc[Edinburgh_Descriptions['Descriptions'] == l, 'subject_code']]*len(Descriptions), ignore_index=True)})  
    Results = Results.append(tests, ignore_index = True)
    i=i+1
    print(round(i*100/len(Edinburgh_Descriptions)))
    if i==1: 
        print(tests[0:10])

Results.to_csv("Word2Vec_Experiment_Results.csv")


