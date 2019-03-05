# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:10:16 2019

@author: Jayesh Jain
"""

import os
from collections import Counter
os.chdir("C:/Users/Jayesh Jain/Downloads")

with open("romeo.txt","wt") as file:
    file.write("Hello i am Romeo \n")
    file.write("Hello i am Juliet")
with open("romeo.txt","rt") as file:
    for line in file:
        frequency = Counter(line.split(" "))
        print("frequency of word in line",frequency)


