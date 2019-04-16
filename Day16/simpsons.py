# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:06:43 2019

@author: Jayesh Jain
"""

import os
import re
os.chdir("C:/Users/Jayesh Jain/Downloads/python files")

with open("simpsons_phone_book.txt","rt") as file:
    for line in file.readlines():
        if re.match(r'^J\w+\ [Neu]+',line):
            print(line)
            