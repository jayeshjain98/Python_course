# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:06:16 2019

@author: Jayesh Jain
"""

week_ = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
input_tup = input("enter tuple of days : ")
for day in week_:
    if day not in input_tup:
        print(week_)
        break

