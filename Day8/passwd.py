# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 00:49:15 2019

@author: Jayesh Jain
"""


import os
os.chdir ="C:/Users/Jayesh Jain/Downloads"

dict1 = {}
with open("passwd","rt") as file:
    for line in file:
        content = line.split(":")
        if content[0] == "#":
            pass
        else:
            dict1[content[0]] = int(content[2])
print(dict1)