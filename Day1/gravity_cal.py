# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:53:50 2019

@author: Jayesh Jain
"""

#let's assume current position of object is 100m 
#the object falls for 10 seconds
height_obj = float(input("enter current height of object "))
new_height = 1000.0 + (-9.81*10*10)/2
print("height of object from ground",new_height)