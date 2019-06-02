# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:50:14 2019

@author: Jayesh Jain
"""
"""Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat")

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
"""

# import the required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts

# load the data 
df = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delimiter =" ")
df2 = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delimiter =" ")

# split data into features and labels
features = df.iloc[:,:-1]
labels = df.iloc[:,-1]

# divide data into training and test data
features_train, features_test, labels_train, labels_test = tts(features, labels, test_size = 0.2, random_state = 0)

# apply linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
# fit the model with training data
regressor.fit(features_train, labels_train)
# predict values with test data
labels_pred = regressor.predict(features_test)

# calculate score train and test
train_score = regressor.score(features_train, labels_train)
test_score = regressor.score(features_test, labels_test)


from sklearn import metrics
print ("Simple Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, labels_pred),2) )


from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
lm_lasso = Lasso() 
lm_ridge =  Ridge() 

lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)

pred_lasso = lm_lasso.predict(features_test)
pred_ridge = lm_ridge.predict(features_test)

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, pred_lasso),2) )

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, pred_ridge),2) )


#---------------------------part (b)-----------------------------------------

mean = df2["lpsa"].mean()
df2["lpsa"] = df2["lpsa"].apply(lambda x:1 if x>=mean  else 0)

features = df2.iloc[:,:-1]
labels = df2.iloc[:,-1]

from sklearn.model_selection import train_test_split as tts
features_train, features_test, labels_train, labels_test = tts(features, labels, test_size = 0.2, random_state = 0)


from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred2 = classifier.predict(features_test)

train_score = classifier.score(features_train, labels_train)
test_sccore = classifier.score(features_test, labels_test)