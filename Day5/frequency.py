# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 23:43:39 2019

@author: Jayesh Jain
"""

user_input = list(input("enter any string : "))
print(user_input.sort())
dict1 = {}
for i in user_input:
    dict1[i] = dict1.get(i,0)+1
print(dict1)
    