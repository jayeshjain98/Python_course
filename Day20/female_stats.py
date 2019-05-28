# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:25:21 2019

@author: Jayesh Jain
"""

# Importing the libraries
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Female_Stats.csv')

features = dataset.iloc[:,1:].values
labels = dataset.iloc[:,0].values

#apply OLS model
# Building the optimal model using Backward Elimination
import statsmodels.api as sm

#adds a constant column to input data set.
features = sm.add_constant(features)


features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
pvalues = regressor_OLS.pvalues.tolist()

#Check significance of both predictors
for i in pvalues:
    if i>0.05:
        print("both predictor are not significant")
        break
    else:
        pass
    print("both predictor are significant")

#get coefficient values
coef_ = regressor_OLS.params.tolist()

#if father hieght is held constant
print("if father hieght is held constant the Average Student Height Increases By:",coef_[1])

#if Mother hieght is held constant
print("if mother hieght is held constant the Average Student Height Increases By:",coef_[2])
