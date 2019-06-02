# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:38:38 2019

@author: Jayesh Jain
"""
"""tree_addhealth.csv

Q1. (Create a program that fulfills the following specification.)

For this Code Challenge, The National Longitudinal Study of Adolescent to Adult Health (Add Health) data set, an ongoing (longitudinal) survey study that began in the mid-1990s is used. The project website URL is:

http://www.cpc.unc.edu/projects/addhealth/.

This large data set is available online from the University of North Carolina’s Carolina Population Center, http://www.cpc.unc.edu/projects/addhealth/data.

 

Import tree_addhealth.csv

 

The attributes are:

 

BIO_SEX: 1 = male 0 = female    

HISPANIC: 1=Yes,0=No    

WHITE : 1=Yes,0=No

BLACK : 1=Yes,0=No          

NAMERICAN: 1=Yes,0=No                      

ASIAN: 1=Yes,0=No                      

ALCEVR1: ever drank alcohol(1=Yes,0=No)   

marever1: ever smoked marijuana(1=Yes,0=No)    

cocever1: ever used cocaine(1=Yes,0=No)                

inhever1: ever used inhalants(1=Yes,0=No)             

cigavail: cigarettes available in home(1=Yes,0=No)

PASSIST: parents or public assistance(1=Yes,0=No)

EXPEL1: ever expelled from school(1=Yes,0=No)

TREG1: Ever smoked regularly(1=Yes,0=No)

Explanatory Variables:

Age

ALCPROBS1:alcohol problems 0-6

DEP1: depression scale

ESTEEM1: self esteem scale       

VIOL1:violent behaviour scale

DEVIANT1: deviant behaviour scale     

SCHCONN1: school connectedness scale       

GPA1: gpa scale  4 points)

FAMCONCT: family connectedness scale       

PARACTV:parent activities scale

PARPRES:parental presence scale

 

    Build a classification tree model evaluating if an adolescent would smoke regularly or not based on: gender, age, (race/ethnicity) Hispanic, White, Black, Native American and Asian, alcohol use, alcohol problems, marijuana use, cocaine use, inhalant use, availability of cigarettes in the home, depression, and self-esteem.

    Build a classification tree model evaluation if an adolescent gets expelled or not from school based on their Gender and violent behavior.
    Use random forest in relation to regular smokers as a target and explanatory variable specifically with Hispanic, White, Black, Native American and Asian.

(Please make confusion matrix and also check accuracy score for each and every section)
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split as TTS
from sklearn.metrics import confusion_matrix, accuracy_score


data = pd.read_csv("tree_addhealth.csv")

# Removing NaN values with Most Frequent value of the column
for i in data:
    data[i] = data[i].fillna(data[i].mode()[0])

#--------------------------Solution part1-------------------------------------
# Separating Dependent and Independent variables as per Problem Statement
features = data[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN',
           'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail',
           'DEP1','ESTEEM1']].values
labels = data["TREG1"].values

# Splitting the Data into Test and Train
features_train,features_test,labels_train,labels_test = TTS(features,labels,test_size=.2,random_state=0)

# Applying DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion="entropy",random_state=0)
classifier.fit(features_train,labels_train)
pred = classifier.predict(features_test)
pd.DataFrame(pred, labels_test)

cm = confusion_matrix(pred, labels_test)
accuracy = accuracy_score(pred, labels_test)

#--------------------------Solution part2-----------------------------------

# Separating Dependent and Independent variables as per Problem Statement
features2 = data[["BIO_SEX","VIOL1"]].values
labels2 = data["EXPEL1"].values

# Splitting the Data into Test and Train
features2_train,features2_test,labels2_train,labels2_test = TTS(features2,labels2,test_size=.2,random_state=0)

# Applying DecisionTreeClassifier
classifier.fit(features2_train,labels2_train)
pred2 = classifier.predict(features2_test)

# Building Confusion Matrix
cm = confusion_matrix(pred2,labels2_test)

# Getting Accuracy Score of the Model
acc_model_part2 = accuracy_score(labels2_test,pred2)

print ("Accuracy Score of the Model part 2 : "+str(round(acc_model_part2*100,2))+"%")

#--------------------------Solution part3-----------------------------------


# Separating Dependent and Independent variables as per Problem Statement
features3 = data[['WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN']].values
lables3 = data["TREG1"].values

features3_train,features3_test,labels3_train,labels3_test = TTS(features3,lables3,test_size=.2,random_state=0)

# Applying RandomForestClassifier
regressor = RandomForestClassifier(n_estimators=10,criterion="entropy", 
                                random_state=0)
regressor.fit(features3_train,labels3_train)
pred3 = regressor.predict(features3_test)

# Building Confusion Matrix
cm = confusion_matrix(pred,labels3_test)

# Getting Accuracy Score of the Model
acc_model_part3 = accuracy_score(labels3_test,pred3)

print ("Accuracy Score of the Model part 3 : "+str(round(acc_model_part3*100,2))+"%")


