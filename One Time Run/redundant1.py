# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 23:10:29 2018

@author: mbrackenrig
"""



from setup import SLOs
ED_list = numpy.zeros(shape = (135,5000))
z=0
for l in Edinburgh_Descriptions.Learning_outcomes:

    test_query = l
    #remove punctuation, numbers, convert to lower case and lemmatize
    test_query = test_query.replace('[^\w\s]','')
    test_query = test_query.replace('\d+','')
    test_query  = test_query.lower()
    test_query = " ".join(lemmatize_sentence(test_query))
    test= test_query.split(" ")

    bigrams = [b for  b in zip(test_query.split(" ")[:-1], test_query.split(" ")[1:])]

    for i in range(0,len(bigrams)):
        bigrams[i] = " ".join(bigrams[i])

    test = test+bigrams
   
    query = numpy.zeros(shape = (1,len(featurenames)))
    for i in range(0,len(test)):
        if test[i] in featurenames:
            query[0,featurenames.index(test[i])] = 1
 
    results = numpy.matmul(query,svdMatrix)
    q = numpy.matmul(results,svdsk)
    del(results)
    ED_list[z,] = q        
    z = z+1
    print(z)
    #So q is my vector representation of the query
UTS_list = numpy.zeros(shape = (3389,5000))
z = 0
for l in SLOs.SLOs:

    test_query = str(l)
    #remove punctuation, numbers, convert to lower case and lemmatize
    test_query = test_query.replace('[^\w\s]','')
    test_query = test_query.replace('\d+','')
    test_query  = test_query.lower()
    test_query = " ".join(lemmatize_sentence(test_query))
    test= test_query.split(" ")

    bigrams = [b for  b in zip(test_query.split(" ")[:-1], test_query.split(" ")[1:])]

    for i in range(0,len(bigrams)):
        bigrams[i] = " ".join(bigrams[i])

    test = test+bigrams
   
    query = numpy.zeros(shape = (1,len(featurenames)))
    for i in range(0,len(test)):
        if test[i] in featurenames:
            query[0,featurenames.index(test[i])] = 1
 
    results = numpy.matmul(query,svdMatrix)
    q = numpy.matmul(results,svdsk)
    del(results)
    
    UTS_list[z,] = q        
    z = z+1
    print(z*100/3389)
    #So q is my vector representation of the query

#this may need to be a loop
results = [cosine_similarity(i,l) for i in ED_list for l in UTS_list]
ED = [Edinburgh_Descriptions.loc[Edinburgh_Descriptions['Descriptions']==i,'subject_code'] for i in ED_list for l in UTS_list]
UTS = [Descriptions.loc[Descriptions['Descriptions']==l,'subject_code'] for i in ED_list for l in UTS_list]

experiment_3_results = pandas.DataFrame({'UTS': UTS, "ED": ED,"similarity":results})
experiment_3_results.to_csv("Experiments/Results/experiment3results.csv")