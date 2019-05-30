# -*- coding: utf-8 -*-
"""
Created on Wed May 29 18:19:51 2019

@author: Jayesh Jain
"""

#import requiered libraries
import pandas as pd
import numpy as np

#collect data
df = pd.read_csv("mushrooms.csv")

features = df.iloc[:,[5,21,22]].values
labels = df.iloc[:,0].values

#label encode features and labels
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels = labelencoder.fit_transform(labels)
features[:,0] = labelencoder.fit_transform(features[:,0])
features[:,1] = labelencoder.fit_transform(features[:,1])
features[:,2] = labelencoder.fit_transform(features[:,2])

#split data into train and test data 
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

#scale all the the columns
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

#-------------------------------------------------------------------------------

#try Logistic regression model for following data
"""from sklearn.linear_model import LogisticRegression
regressor = LogisticRegression()
regressor.fit(features_train, labels_train)
labels_pred = regressor.predict(features_test)
cm = confusion_matrix(labels_test, labels_pred)

#model's accuracy
regressor.score(features_test, labels_test)
"""
#-------------------------------------------------------------------------------
#use KNN classification model
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2)
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
