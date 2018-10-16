# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 17:46:26 2018

@author: mbrackenrig
"""

#LSA in Python
import os

os.chdir('C:/Users/mbrackenrig/Desktop/University/Sem2_18/iLab/iLab_Repository')

from setup import  skills,  Descriptions, Edinburgh_Descriptions

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

#We will get to this a litle later.


