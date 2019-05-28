# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:22:08 2019

@author: Jayesh Jain
"""
#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#collect data from file
data = pd.read_csv("bluegills.csv")

#separatee features and lables
features = data.iloc[:,:-1].values
lables = data.iloc[:,-1].values

#observe pattern of fish height
plt.scatter(features, lables, c="red", alpha=0.5)

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression

#fitting polynomial regression model to the data
from sklearn.preprocessing import PolynomialFeatures 
poly_obj = PolynomialFeatures(degree = 7)

#update features as polynomial features
polynomial_features = poly_obj.fit_transform(features)

#fit polynomial features in linear regression model
lin_reg = LinearRegression()
lin_reg.fit(polynomial_features,lables)

# Visualising the Polynomial Regression results
plt.scatter(features, lables, color = 'red')
plt.plot(features, lin_reg.predict(poly_obj.fit_transform(features)), color = 'blue')

#predicting result 
x = np.array([[5]])
Pred = lin_reg.predict(poly_obj.transform(x))
print("the length of a randomly selected five-year-old bluegill fish:",Pred)