# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:17:17 2019

@author: Jayesh Jain
"""

input_ = int(input("enter any number "))
for i in range (1,input_+1):
    print(" *"*i)
    if i == input_:
        while(i>0):
            print(" *"*(i-1))
            i = i-1
    