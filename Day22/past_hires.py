# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:31:47 2019

@author: Jayesh Jain
"""
"""Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.
"""

# import required libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split as tts

# load the data
df = pd.read_csv("PastHires.csv")

# remove the categorical data from dataset 
labelencoder = LabelEncoder()
labelencoder1 = LabelEncoder()
df.iloc[:,[1]] = labelencoder.fit_transform(df.iloc[:,[1]])
df.iloc[:,[4]] = labelencoder.transform(df.iloc[:,[4]])
df.iloc[:,[5]] = labelencoder.transform(df.iloc[:,[5]])
df.iloc[:,[6]] = labelencoder.transform(df.iloc[:,[6]])
df.iloc[:,[3]] = labelencoder1.fit_transform(df.iloc[:,[3]])

# define features and labels
features = df.iloc[:,:-1]
labels = df.iloc[:,-1]

# split training and testing data
features_train, features_test, labels_train, labels_test = tts(features, labels, test_size=0.2, random_state = 0)

# convert data to standard scale
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
features_train = ss.fit_transform(features_train)
features_test = ss.transform(features_test)

# apply Decision tree model 
from sklearn.tree import DecisionTreeClassifier
classi = DecisionTreeClassifier()
# fit training data into model
classi.fit(features_train, labels_train)
# predict values through model
labels_pred = classi.predict(features_test)
# observe score of the model
score1 = classi.score(features_test, labels_test)

# apply random forest model
from sklearn.ensemble import RandomForestClassifier
classi2 = RandomForestClassifier(n_estimators=10, random_state=0)
# fit model with training data
classi2.fit(features_train, labels_train)
# predict values using model
labels_pred2 = classi2.predict(features_test)
# observe score of the model
score2 = classi2.score(features_test, labels_test)

# observe prediction for new input data
x = [10,labelencoder.transform([["Y"]]),4,labelencoder1.transform([["BS"]]),labelencoder.transform([["Y"]]),labelencoder.transform([["N"]])]
x = np.array(x).reshape(1,-1)
y = [10,labelencoder.transform([["N"]]),4,labelencoder1.transform([["MS"]]),labelencoder.transform([["N"]]),labelencoder.transform([["Y"]])]
y = np.array(y).reshape(1,-1)

labels_pred3 = classi2.predict(x)
labels_pred3 = classi2.predict(y)


        
    
    








