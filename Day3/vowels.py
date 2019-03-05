# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:06:54 2019

@author: Jayesh Jain
"""
new = []
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowel_list = ['a','e','i','o','u','A','E','I','O','U']
for i in state_name:
    for j in i:
        if j in vowel_list:
            i = i.replace(j, "")
    new.append(i)
print(new)
    
