# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:37:33 2019

@author: Jayesh Jain
"""

import numpy as np
input_= input("enter space separated inputs: ")  #take only 9 space separated no.
list_=input_.split(" ")                          #create list of inputs
new_list=list(map(int, list_))
x = np.array( new_list)
y=x.reshape(3,3) 
print(y)

