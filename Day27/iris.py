# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:19:06 2019

@author: Jayesh Jain
"""

"""
Q2. (Create a program that fulfills the following specification.)

The iris data set consists of 50 samples from each of three species of Iris flower (Iris setosa, Iris virginica and Iris versicolor).



    Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres (iris.data).
    Import the iris dataset already in sklearn module using the following command:\


from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data


Reduce dimension from 4-d to 2-d and perform clustering to distinguish the 3 species.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
irises = pca.fit_transform(iris)

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(irises)

# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(irises[pred_cluster == 0, 0], irises[pred_cluster == 0, 1], c = 'blue', label = 'low crime')
plt.scatter(irises[pred_cluster == 1, 0], irises[pred_cluster == 1, 1], c = 'red', label = 'high crime')
plt.scatter(irises[pred_cluster == 2, 0], irises[pred_cluster == 2, 1], c = 'green', label = 'medium crime')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Crime_Data')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()






















