# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:47:45 2019

@author: Jayesh Jain
"""
"""Q1. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. How would you figure out the actual size of these 3 types of shirt to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of the data as stated above.
"""
# import libraries
import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("tshirts.csv")
features = df.iloc[:,[1,2]].values

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()

# Fitting K-Means to the dataset
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'medium')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'large')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'small')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('T-Shirts Sizes')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.legend()
plt.show()

print("Standardized value for small sized tshirts is height",kmeans.cluster_centers_[2, 0],"weight", kmeans.cluster_centers_[2, 1])
print("Standardized value for medium sized tshirts is height",kmeans.cluster_centers_[0, 0],"weight", kmeans.cluster_centers_[0, 1])
print("Standardized value for large sized tshirts is height",kmeans.cluster_centers_[1, 0],"weight", kmeans.cluster_centers_[1, 1])