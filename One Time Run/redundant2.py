# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 23:14:23 2018

@author: mbrackenrig
"""

results = [cosine_similarity(i,l) for i in ED_list for l in UTS_list]
ED = [Edinburgh_Descriptions.loc[Edinburgh_Descriptions['Descriptions']==i,'subject_code'] for i in ED_list for l in UTS_list]
UTS = [Descriptions.loc[Descriptions['Descriptions']==l,'subject_code'] for i in ED_list for l in UTS_list]

experiment_3_results = pandas.DataFrame({'UTS': UTS, "ED": ED,"similarity":results})
experiment_3_results.to_csv("Experiments/Results/experiment3results.csv")
#for l in range(0, len(ED_list)):

from setup import SLOs
import pandas

import spacy

nlp = spacy.load('en_core_web_lg')

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

Results.to_csv("C:/Users/mbrackenrig/Desktop/University/Sem2_18/iLab/iLab_Repository/Experiments/Results/Experiment_1_Results_SLOs_second.csv")

