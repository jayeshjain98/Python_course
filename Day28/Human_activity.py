# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 16:14:00 2019

@author: Jayesh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv("train.csv")
df2 = pd.read_csv("test.csv")

features_train = df1.iloc[:,:-2]
labels_train = df1.iloc[:,-1]
features_test = df2.iloc[:,:-2]
labels_test = df2.iloc[:,-1]

#------------------------part a----------------------------------------------

from sklearn.tree import DecisionTreeClassifier
classifier1 = DecisionTreeClassifier()  
classifier1.fit(features_train, labels_train)

labels_pred01 = classifier1.predict(features_test)  
score_t1 = classifier1.score(features_train, labels_train)
score_te1 = classifier1.score(features_test, labels_test)


#-----------------------------------part b-------------------------------------

from sklearn.ensemble import RandomForestClassifier
classifier2 = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier2.fit(features_train, labels_train)  
labels_pred2 = classifier2.predict(features_test)
score_tr2 = classifier2.score(features_train, labels_train)
score_te2 = classifier2.score(features_test, labels_test)

#---------------------------------------part c--------------------------------

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier3 = LogisticRegression()
classifier3.fit(features_train, labels_train)

# Predicting the class labels
labels_pred3 = classifier3.predict(features_test)

score_tr3 = classifier3.score(features_train, labels_train)
score_te3 = classifier3.score(features_test, labels_test)

#------------------------------part d--------------------------------------

# Fitting kNN Regression to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier4 = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier4.fit(features_train, labels_train)

# Predicting the class labels
labels_pred4 = classifier4.predict(features_test)

score_tr4 = classifier4.score(features_train, labels_train)
score_te4 = classifier4.score(features_test, labels_test)



#--------------------------part e--------------------------------------------

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels_train = labelencoder.fit_transform(labels_train)
labels_test = labelencoder.transform(labels_test)






# Building the optimal model using Backward Elimination
import statsmodels.api as sm
features_train = sm.add_constant(features_train)

clms=list(range(562))

while(True):
    features_opt = features_train.iloc[:,clms]
    regressor_OLS = sm.OLS(endog = labels_train, exog = features_opt.values).fit()
    value = np.max(regressor_OLS.pvalues)
    indx = np.argmax(regressor_OLS.pvalues)
    if not value or value<=.05:
        break
    del clms[indx]
print(clms)

features_train = features_train.iloc[:,clms]
features_test = sm.add_constant(features_test)
features_test = features_test.iloc[:,clms]

#------------------------part a----------------------------------------------

from sklearn.tree import DecisionTreeClassifier
classifier01 = DecisionTreeClassifier()  
classifier01.fit(features_train, labels_train)

labels_pred01 = classifier01.predict(features_test)  
score_tr01 = classifier01.score(features_train, labels_train)
score_te01 = classifier01.score(features_test, labels_test)


#-----------------------------------part b-------------------------------------

from sklearn.ensemble import RandomForestClassifier
classifier02 = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier02.fit(features_train, labels_train)  
labels_pred02 = classifier02.predict(features_test)
score_tr02 = classifier02.score(features_train, labels_train)
score_te02 = classifier02.score(features_test, labels_test)

#---------------------------------------part c--------------------------------

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier03 = LogisticRegression()
classifier03.fit(features_train, labels_train)

# Predicting the class labels
labels_pred03 = classifier03.predict(features_test)

score_tr03 = classifier03.score(features_train, labels_train)
score_te03 = classifier03.score(features_test, labels_test)

#------------------------------part d--------------------------------------

# Fitting kNN Regression to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier04 = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier04.fit(features_train, labels_train)

# Predicting the class labels
labels_pred04 = classifier04.predict(features_test)

score_tr04 = classifier04.score(features_train, labels_train)
score_te04 = classifier04.score(features_test, labels_test)

#---------------------------visualization-----------------------------------

models = ["Decision Tree", "Random Forest", "Logistic Regression", "kNN"]
scores = ["score_te1","score_te2","score_te3","score_te4"]
scores = ["score_te01","score_te02","score_te03","score_te04"]


ind = np.arange(4)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind,[score_te1,score_te2,score_te3,score_te4], width, color='blue')

rects2 = ax.bar(ind + width,[score_te01,score_te02,score_te03,score_te04], width, color='red')

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_ylabel("Classification Models")
ax.set_title('Comparision Of Score')
ax.set_xticks(ind + width / 2)

ax.set_xticklabels(('DecisionTree', 'RandomForest', 'LogisticRegression', 'KNN'),rotation = 45)

ax.legend((rects1[0], rects2[0]), ('Before OLS', 'OLS'))










