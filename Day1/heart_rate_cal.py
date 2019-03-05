# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:34:35 2019

@author: Jayesh Jain
"""

#let's assume my age is 21
my_age = int(input("enter your age "))
max_heart_rate = 220 - my_age
lower_end = (70*max_heart_rate)/100
higher_end = (85*max_heart_rate)/100
print("maximum heart rate ",max_heart_rate)
print("lower end of target heart rate", lower_end)
print("higher end of target heart rate", higher_end)
