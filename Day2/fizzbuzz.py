# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 19:12:14 2019

@author: Jayesh Jain
"""
i=1
while(i<101):
    if i%3==0:
        print("FIZZ")
    elif i%5==0 and i%3==0:
        print("FIZZBUZZ")
    elif i%5==0:
        print("BUZZ")
    else:
        print(i)
    i = i+1