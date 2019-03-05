# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 00:34:25 2019

@author: Jayesh Jain
"""

import os
os.chdir ="C:/Users/Jayesh Jain/Downloads"

def final_line(filename):
    list1 = []
    with open(filename,"rt") as file:
        for line in file:
            list1.append([line])
    last_line = list1.pop()
    return last_line

final_line("romeo.txt")            