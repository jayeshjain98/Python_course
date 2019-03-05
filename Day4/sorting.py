# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:09:54 2019

@author: Jayesh Jain
"""

entries = int(input("enter no entries:"))
new_list = []
for i in range (0,entries):
    entry = tuple(input("enter the details: ").split(","))
    new_list.append(entry)
print("entered list:",new_list)

result = sorted(new_list,key = lambda t:(t[0],t[1],t[2]))
print("sorted list:",result)

