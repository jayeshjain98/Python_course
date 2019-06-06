# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:29:19 2019

@author: Jayesh Jain
"""
"""Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values before fitting the data to model, remove the null values from each row and perform the associations once again.
Also draw the bar chart of top 10 edibles.
"""
import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt

df = pd.read_csv("Market_Basket_Optimisation.csv", header = None)

transactions = df.apply(lambda x: x.dropna().tolist(), axis=1).tolist()

"""
list1 = []
[list1.append(df.iloc[j,:].values.tolist()) for j in range(0,7501)]
list2 = []
for i in list1:
    list2.append(list(filter(lambda x: str(x)!="nan",i)))
   """ 
# Training Apriori on the dataset

rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

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
    
a=[]
for i in transactions:
    for j in i:
        a.append(j)
        
b = pd.DataFrame(a)
top_edibles = b.iloc[:,0].value_counts().head(10)
names = top_edibles.index.tolist()
values = top_edibles.tolist()

plt.bar(names, values, align='center', alpha=0.5)
plt.xticks(rotation=90)

plt.title('Top_10_edibles')

plt.show()

    
