# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 19:52:45 2018

@author: mbrackenrig
"""

#Lets try something fun

#LSA in Python
import os

os.chdir('C:/Users/mbrackenrig/Desktop/University/Sem2_18/iLab/iLab_Repository')

from setup import CILOs, SLOs, Subjects, skills, skillGroups, Descriptions, occupations

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
skills.description = skills.description.str.replace('[^\w\s]','')

#remove numeric
skills.description = skills.description.str.replace("\d+", "")

#Change to lowercase
skills.description = skills.description.str.lower()

#not sure I want to remove stop words yet
from nltk.corpus import stopwords
stop = stopwords.words('english')
skills.description = skills.description.apply(lambda x: " ".join(x for x in x.split() if x not in stop))


skills.description = skills.description.apply(lambda x: " ".join(lemmatize_sentence(x)))

#Lets create a DTM
dtMatrix = cv.fit_transform(skills.description).transpose().toarray()
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
svd = TruncatedSVD(n_components = 5000, random_state=42)
#svdMatrix = svd.fit_transform(tfidftranspose)
svdMatrix = svd.fit_transform(tfidfMatrix)
#print(svdMatrix)
import numpy
svdsk = numpy.diag(svd.singular_values_)
svdvk = svd.components_

SLO_index = 36103
#We will get to this a litle later.


test_query = Descriptions.loc[Descriptions['subject_code'] == SLO_index, 'Descriptions']


#remove punctuation, numbers, convert to lower case and lemmatize
test_query = test_query.replace('[^\w\s]','')

test_query = test_query.replace('\d+','')

test_query  = test_query.str.lower()

test_query = "this subject helps students to advance their thinking about statistics and how it can be used, or abused, in data science. starting from the assumed knowledge of basic statistics that students bring into the subject: including concepts like probability, distributions, hypothesis testing, significance, power and confidence; students quickly develop their ability to create modern statistical models in real-world data science contexts. learning to use the powerful language r, students work their way through the entire data science cycle: from data collection, cleaning and merging datasets, exploratory analysis, modelling and reporting. this process provides rapid exposure to the wide range of modern day packages (for example, the tidyverse) that facilitate rapid statistical analyses for data science questions. students also learn to make the invisible trends in datasets visible, to make predictions from complex datasets and to reproducibly document their statistical procedures for different audiences. working with a team of data science professionals from a variety of different backgrounds, students learn how to appropriately communicate their newfound statistical insights and engage a variety of different audiences and stakeholders in order to inform decision making. a selection of advanced topics helps each student to concurrently follow their own personalised learning journey: evaluating and bolstering any gaps in their knowledge and skills, and prepare for future electives and ilab projects."
test_query = " ".join(lemmatize_sentence(test_query))

test= test_query.split(" ")

bigrams = [b for  b in zip(test_query.split(" ")[:-1], test_query.split(" ")[1:])]


for i in range(0,len(bigrams)):
    bigrams[i] = " ".join(bigrams[i])

test = test+bigrams
   
import pandas

query = numpy.zeros(shape = (1,len(featurenames)))
for i in range(0,len(test)):
    if test[i] in featurenames:
        query[0,featurenames.index(test[i])] = 1

 
results = numpy.matmul(query,svdMatrix)


q = numpy.matmul(results,svdsk)

del(results)

cosine = cosine_similarity(q, svdvk.transpose())


cosine_df = pandas.DataFrame({'cosine': cosine[0,]})
doc = numpy.argmax(cosine[0,])

sorts = cosine_df.nlargest(10,'cosine')

print(str(Descriptions.loc[Descriptions['subject_code'] == SLO_index, 'Descriptions']))
#print(SLOs.subject_code[SLO_index])
print(skills.preferredLabel[sorts.index[0:20]])

print(skills.description[doc])
print(skills.preferredLabel[doc])
#print(skills.altLabels[doc])
#print(test_query)
#print(skills.preferredLabel[2003])
print(SLOs.subject_code[SLO_index])