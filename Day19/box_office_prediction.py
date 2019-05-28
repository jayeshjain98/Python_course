# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:31:20 2019

@author: Jayesh Jain
"""

#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt

#Importing data

dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')

features = dataset.iloc[:,0].values.reshape(9,1)

labels_1 = dataset.iloc[:,1].values
labels_2 = dataset.iloc[:,2].values


#Importing LinearRegression Model

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor_1 = LinearRegression()
regressor.fit(features, labels_1)
regressor_1.fit(features, labels_2)

if(regressor.predict([[10]])>regressor_1.predict([[10]])):
    print("Bahubali_2 earns more on the tenth day")
else:
    print("Dangal earns more on the tenth day")