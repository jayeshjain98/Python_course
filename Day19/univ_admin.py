# -*- coding: utf-8 -*-
"""
Created on Tue May 28 09:11:21 2019

@author: Jayesh Jain
"""

import pandas as pd

# Importing the dataset
dataset = pd.read_csv('University_data.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

#Check if any NaN values in dataset
  

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

# Avoiding the Dummy Variable Trap
# dropping first column
features = features[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.1, random_state = 0)


#preparing linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

#using prepared model to predict values
pred = regressor.predict(features_test)

#compairing predicted values with actual values
print (pd.DataFrame({"Pred":pred, "Labels_test":labels_test}))





