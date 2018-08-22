# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 19:52:45 2018

@author: mbrackenrig
"""

#Lets try something fun

#LSA in Python

#import some fun stuff
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

#What is a count vectorizer
?CountVectorizer

cv = CountVectorizer(input= 'content') #I assume this to be content as we will be analysising strings in a DF not files.

#Lets create a DTM
dtMatrix = cv.fit_transform(skills.description).toarray()
#Inspect it
print(dtMatrix.shape)
#Print the names of the skills
featurenames = cv.get_feature_names()
print(featurenames)

#Create a tf-idf
tfidf = TfidfTransformer()
#Turn DTM into tf-idf matrix
tfidfMatrix = tfidf.fit_transform(dtMatrix).toarray()
print(tfidfMatrix.shape)

#SVD is dimensionality reduction down to a managable set

#Reduces the vector space to 100 'terms'
svd = TruncatedSVD(n_components = 100)
svdMatrix = svd.fit_transform(tfidfMatrix)

print(svdMatrix)

#Create the cosine similarity - This doesnt work!!!!
#cosine = cosine_similarity(svdMatrix[1], svdMatrix)


