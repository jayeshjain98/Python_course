# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:43:36 2019

@author: Jayesh Jain
"""
"""Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score
"""

# import all the required libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split as tts

# load the dataset
df = pd.read_csv("kc_house_data.csv")

# extract year from the date column
df["date"] = pd.to_numeric(df["date"].apply(lambda x: x[:4]))
# drop id column
df = df.drop("id", axis=1)
# check for null values
df.isnull().any(axis=0)
# remove null with most frequent values
df['sqft_above'] = df["sqft_above"].fillna(df["sqft_above"].mode()[0])

# split data into features and labels
features = df.drop("price", axis=1).values
labels = df["price"].values


# This is done because statsmodels library requires it to be done for constants.
features = sm.add_constant(features)
# create list of no. of columns in features
clms=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

# get the most useful columns in prediction
while(True):
    features_opt = features[:,clms]
    regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
    indx = np.argmax(regressor_OLS.pvalues)
    if regressor_OLS.pvalues[indx] <= .05:
        break
    del clms[indx]
print(clms)
# new features obtained
features = features[:,clms]

features_train, features_test, labels_train, labels_test = tts(features, labels, test_size = 0.2, random_state = 0)

# apply regression and regularization models for overfitting
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
lm = LinearRegression ()
lm_lasso = Lasso() 
lm_ridge =  Ridge()

# fit the models with training data
lm.fit(features_train, labels_train)
lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)

# predict values for the test data
lm_pred = lm.predict(features_test)
lm_lasso_pred = lm_lasso.predict(features_test)
lm_ridge_pred = lm_ridge.predict(features_test)

# mean_squared_error for above models
from sklearn import metrics
print(metrics.mean_squared_error(labels_test,lm_pred))
print(metrics.mean_squared_error(labels_test,lm_lasso_pred))
print(metrics.mean_squared_error(labels_test,lm_ridge_pred))




