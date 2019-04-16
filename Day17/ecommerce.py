# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:00:10 2019

@author: Jayesh Jain
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100, 20, 10000)
print (incomes)

print("Mean value is: ", np.mean(incomes))                              #Mean transaction amount
print("Median value is: ", np.median(incomes))                          #Median transaction amount
print("Standard Deviation is: ", np.std(incomes))
print("Correlation coefficient value is: ", np.corrcoef(incomes))

plt.hist(incomes, 50)
plt.show()