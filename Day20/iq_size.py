# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 18:17:59 2019

@author: Jayesh Jain
"""

#import pandas and numpy library for data manupulation and visualisation
import pandas as pd
import numpy as np

dataset = pd.read_csv("iq_size.csv")
features = dataset.iloc[:,1:].values
labels = dataset.iloc[:,0].values

#import train_test_split to divide dat into training and testing data
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
#This is done because statsmodels library requires it to be done for constants.
features = np.append(arr = np.ones((38, 1)), values = features, axis = 1)

#create list of no. of columns in features
clms=[0,1,2,3]

while(True):
    features_opt = features[:,clms]
    regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
    indx = np.argmax(regressor_OLS.pvalues)
    if regressor_OLS.pvalues[indx]<=.05:
        break
    del clms[indx]
    print(clms)

features = features[:,clms]
print("The most useful column in predicting iq is "+dataset.columns.values.tolist()[1])

#import train_test_split to divide dat into training and testing data
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

regressor.predict([[90]])