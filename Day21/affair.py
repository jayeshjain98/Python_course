# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:53:56 2019

@author: Jayesh Jain
"""

#import required libraries
import pandas as pd
import numpy as np

#collect data 
data = pd.read_csv("affairs.csv")

features = data.iloc[:,:-1].values 
labels = data.iloc[:,-1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

#apply onehotencoding on occupation and husb_occupation
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [5,6])
features_train = onehotencoder.fit_transform(features_train).toarray()
features_test = onehotencoder.transform(features_test).toarray()
features_train = np.delete(features_train, [0,6], axis=1)
features_test = np.delete(features_test, [0,6], axis=1)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

#apply logistic regresssion model
from sklearn.linear_model import LogisticRegression
regressor = LogisticRegression()
regressor.fit(features_train,labels_train)
labels_pred = regressor.predict(features_test)
pd.DataFrame(labels_pred, labels_test)

#check confusion matric for your model
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

#accuracy of our model
regressor.score(features_test, labels_test)
women_data = [3,25,3,1,5,16,4,2]
x = np.array(women_data).reshape(1,-1)
y = onehotencoder.transform(x).toarray()
y = np.delete(y, [0,6], axis=1)

#calculate percentage of women who had an affair
women_aff = data[data["affair"]==1]['affair'].count()

percentage = women_aff/data["affair"].count()*100

print("Total women who had an affair:",percentage)


