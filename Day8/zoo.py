# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:37:55 2019

@author: Jayesh Jain
"""

import os
os.chdir("C:/Users/Jayesh Jain/Downloads")

dict1 = {}
name_list = []
a = []
with open("zoo.csv","rt") as file:
    file.readline()
    for line in file:
        
        a =  line.split(",").pop(0)
        dict1[a] = int(line.split(",").pop(2))+dict1.get(a,0)
        if a not in name_list:
            name_list.append(a)
        else:
            pass

print(dict1)

print(name_list)

def get_names(x):
    
    for i in dict1.keys():
        print(i)
get_names(dict1)

def water_need(x):
    for i,j in dict1.items():
        print(i,j)
water_need(dict1)

def total_waterneed(x):
    a = 0
    for i in dict1.values():
        a += i
    return a
total_waterneed(dict1)