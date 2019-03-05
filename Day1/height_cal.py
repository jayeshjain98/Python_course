# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:10:45 2019

@author: Jayesh Jain
"""

#let's assume my height is 5 foot 11 inches
my_height_foot = int(input("height in foot"))
my_height_inch = int(input("height in inches"))
#my height in meters
my_height_meter = (my_height_foot*0.3048) + (my_height_inch*0.0254) 
print(my_height_meter)
#my height in centimeter
my_height_cm = my_height_meter*100
print(my_height_cm)