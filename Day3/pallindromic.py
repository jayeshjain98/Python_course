# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:32:05 2019

@author: Jayesh Jain
"""
new = []
input_ = input("enter space separated integers ")
arr = input_.split(' ')
print(arr)
for i in arr:
    
    if int(i)>=0 and i[::-1] == i:
        new.append(i)
        
if new != None:
    print("True")
            