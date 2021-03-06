# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 13:16:08 2019

@author: Jayesh
"""

"""Q1. Code Challegene (NLP)
Dataset: amazon_cells_labelled.txt


The Data has sentences from Amazon Reviews

Each line in Data Set is tagged positive or negative

Create a Machine learning model using Natural Language Processing that can predict wheter a given review about the product is positive or negative
"""
import pandas as pd
import numpy as np

df = pd.read_csv("amazon_cells_labelled.txt",delimiter = "\t", header = None)

import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
#from nltk.stem.wordnet import WordNetLemmatizer 

corpus = []
for i in range(1000):
    review = re.sub(r'[^a-zA-Z]',' ',df[0][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if word not in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
# Also known as the vector space model
# Text to Features (Feature Engineering on text data)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = df.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)


from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
G = GaussianNB()
B = BernoulliNB()
M = MultinomialNB()
G.fit(features_train, labels_train)
B.fit(features_train, labels_train)
M.fit(features_train, labels_train)


# Predicting the Test set results
labels_pred_G = G.predict(features_test)
labels_pred_B = B.predict(features_test)
labels_pred_M = M.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_nb_g = confusion_matrix(labels_test, labels_pred_G)
cm_nb_b = confusion_matrix(labels_test, labels_pred_B)
cm_nb_m = confusion_matrix(labels_test, labels_pred_M)


print("The best model for Natural Language Processing that can predict wheter a given review about the product is positive or negative is BernoulliNB")

