# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:17:11 2019

@author: Jayesh Jain
"""

import numpy as np
import matplotlib.pyplot as plt
import functools
from math import sqrt
incomes = np.random.normal(150, 20, 1000)
print(incomes)

plt.hist(incomes, 100)
plt.show()
mean = np.mean(incomes)                             #Mean transaction amount
red_inc_lst = map(lambda x:x**2,list(map(lambda x:x-mean,incomes)))
reduce_income =functools.reduce(lambda x,y:x+y,red_inc_lst)
variance = int(reduce_income/1000)
print("variance in income:",variance)
std_dev = sqrt(variance)
print("standard deviation in income is:",std_dev)