# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:04:10 2019

@author: Jayesh Jain
"""

# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

#Importing the data
dataset = pd.read_csv('Foodtruck.csv')

features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(features, labels)

regressor.predict([[3.073]])

# Visualising the Training set results
plt.scatter(features, labels, color = 'red')
plt.plot(features, regressor.predict(features), color = 'blue')
plt.title('Population vs Profit (Training set)')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()