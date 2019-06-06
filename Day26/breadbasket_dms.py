# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:42:44 2019

@author: Jayesh Jain
"""
"""Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from apyori import apriori


df = pd.read_csv("BreadBasket_DMS.csv")


l1 = df.index[df["Item"]=="NONE"].tolist()
df = df.drop(l1,axis=0)

x = df["Item"].value_counts().head(15)

top_name = x.index.tolist()
bought_freq = x.tolist()

plt.pie(bought_freq,autopct="%1.1f%%",labels = top_name,radius =2)

group = df.groupby("Transaction")["Item"].unique().tolist()
group1 = [x.tolist() for x in group]


# Training Apriori on the dataset

rules = apriori(group1, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

# Visualising the results
results = list(rules)


for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")


