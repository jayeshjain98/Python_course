# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 19:06:06 2019

@author: Jayesh Jain
"""

#let's assume marks obtained are A1=80, A2=60, A3=70, E1=80, E2=85
A1=int(input("enter marks "))
A2=int(input("enter marks ")) 
A3=int(input("enter marks ")) 
E1=int(input("enter marks "))
E2=int(input("enter marks "))
weighted_score = (A1 + A2 + A3)*0.1 + (E1 +E2)*0.35
print("total weighted score of student is ", weighted_score)