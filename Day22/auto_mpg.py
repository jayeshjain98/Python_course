# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:32:10 2019

@author: Jayesh Jain
"""
"""Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)
"""

# Importt requried libraries
import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('Auto_mpg.txt', sep="\s+", header=None)

# Give names to the column
data.columns = ["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]

# Display car name with highest mpg
x = data['mpg'].idxmax()
print("The car with highest mpg ",data.iloc[x,-1])


features = data.iloc[:,1:-1]
labels = data.iloc[:,0]

# replace object to numeric value
features["horsepower"] = features["horsepower"].replace("?",data['horsepower'].mode()[0])
features["horsepower"] = pd.to_numeric(features["horsepower"])


# split dataset into training and testing 
from sklearn.model_selection import train_test_split as tts
features_train,features_test,labels_train,labels_test = tts(features,labels,test_size=.2,random_state=0)


#convert data into standard scale
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
features_train = ss.fit_transform(features_train)
features_test = ss.transform(features_test)

# build decision tree model for mpg value
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(features_train, labels_train)
labels_pred = regressor.predict(features_test)
# observe score of the Decision tree model
a = regressor.score(features_test, labels_test)


# build random forest model for mpg value
from sklearn.ensemble import RandomForestRegressor
regressor_ = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor_.fit(features_train, labels_train)  
labels_pred = regressor_.predict(features_test)
# observe score for Random forest model
a_ = regressor_.score(features_test, labels_test)

if a>a_:
    print("Suitable model is DecisionTreeRegressor")
else:
    print("Suitable model is RandomForestRegressor")

# Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)    
print("prediction from random forest:",regressor_.predict(np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1)))

print("prediction from decision tree:",regressor.predict(np.array([6,215,100,2630,22.2,80,3]).reshape(1,-1)))

