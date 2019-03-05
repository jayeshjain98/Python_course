# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:03:14 2019

@author: Jayesh Jain
"""

import os
os.chdir("C:/Users/Jayesh Jain/Downloads")

name_list = []

count = 0
while(True):
    user_input = input("enter name : ")
    if not user_input or count>25:
        break
    name_list.append(user_input)
    name_list.append("\n")
    count += 1

with open("absentee.txt",'wt') as wf:
    wf.writelines(name_list)
file = open("absentee.txt","rt")
file.read()