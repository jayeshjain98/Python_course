# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:30:33 2019

@author: Jayesh Jain
"""
#let's assume my weight is 60 kg and height is 1.0834m

my_weight = int(input("enter weight in kg "))
my_height = float(input("enter height in meter "))
my_ponderal = my_weight/my_height**3
print("my ponderal index is ",my_ponderal)