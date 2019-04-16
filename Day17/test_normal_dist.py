# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:08:24 2019

@author: Jayesh Jain
"""
import re
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
temp_list = []
with open("human_body_temperature.csv","rt") as file:
    for line in file.readlines():
        result = re.findall(r'^[0-9\.]{1,4}',line)
        
        if re.match(r'^[0-9\.]{1,4}',line):
            temp_list.append(float(result[0]))
print(temp_list)

plt.hist(temp_list, 7)
plt.show()

mean = np.mean(temp_list)
print(mean)

median = np.median(temp_list)
print(median)

a = np.array(temp_list)
mode =stats.mode(a)
print(mode)