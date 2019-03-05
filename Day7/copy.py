# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:43:40 2019

@author: Jayesh Jain
"""

import os
os.chdir("C:/Users/Jayesh Jain/Downloads")

with open("anagram.txt","rt") as rf:
    with open("jayesh.txt","wt") as wf:
        for line in rf:
            wf.write(line)
file = open("jayesh.txt","rt")
file.read()