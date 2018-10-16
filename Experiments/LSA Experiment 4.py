# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 14:32:54 2018

@author: mbrackenrig
"""


#LSA in Python
import os

os.chdir('C:/Users/mbrackenrig/Desktop/University/Sem2_18/iLab/iLab_Repository')

from setup import    Descriptions

#import some fun stuff
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from pywsd.utils import lemmatize_sentence

#lets try a bigram vectorizer
cv = CountVectorizer(input= 'content', strip_accents = 'ascii', ngram_range = [1,2], min_df = 2) #I assume this to be content as we will be analysising strings in a DF not files.


#remove punctuation
Descriptions.Descriptions = Descriptions.Descriptions.str.replace('[^\w\s]','')

#remove numeric
Descriptions.Descriptions = Descriptions.Descriptions.str.replace("\d+", "")

#Change to lowercase
Descriptions.Descriptions = Descriptions.Descriptions.str.lower()

#not sure I want to remove stop words yet
from nltk.corpus import stopwords
stop = stopwords.words('english')
Descriptions.Descriptions= Descriptions.Descriptions.apply(lambda x: " ".join(x for x in x.split() if x not in stop))

Descriptions.Descriptions = Descriptions.Descriptions.apply(lambda x: " ".join(lemmatize_sentence(x)))

#Lets create a DTM
dtMatrix = cv.fit_transform(Descriptions.Descriptions).transpose().toarray()
#Inspect it
#print(dtMatrix.shape)
#Print the names of the skills
featurenames = cv.get_feature_names()
#print(featurenames)

#Create a tf-idf
tfidf = TfidfTransformer()
#Turn DTM into tf-idf matrix
tfidfMatrix = tfidf.fit_transform(dtMatrix).toarray()
#print(tfidfMatrix.shape)
del(dtMatrix)
#I think at this point here we need to transpose the matrix
#tfidftranspose = tfidf.fit_transform(dtMatrix).transpose().toarray()
#SVD is dimensionality reduction down to a managable set

#Reduces the vector space to 100 'terms' - recommended in text
svd = TruncatedSVD(n_components = 2000, random_state=42)
#svdMatrix = svd.fit_transform(tfidftranspose)
svdMatrix = svd.fit_transform(tfidfMatrix)
#print(svdMatrix)
import numpy
svdsk = numpy.diag(svd.singular_values_)
svdvk = svd.components_

#We will get to this a litle later.

from setup import Edinburgh_Descriptions
import pandas

#Edinburgh_Descriptions = Edinburgh_Descriptions.drop_duplicates()
#ED_list = numpy.zeros(shape = (135,2000))
Results = pandas.DataFrame({'subject_code': Descriptions.subject_code})
z=0
for l in Edinburgh_Descriptions.Descriptions:

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
    cosine = cosine_similarity(q,svdvk.transpose())
    cosine_df = pandas.DataFrame({z: cosine[0,]})
    Results = Results.join(cosine_df)
    del(results)
    #ED_list[z,] = q        
    z = z+1
    print(z)


Results.to_csv("Experiment_4_Results.csv")



