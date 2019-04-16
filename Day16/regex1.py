# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:47:40 2019

@author: Jayesh Jain
"""

import re
input_ = input("enter any no. to check if it is floating no. or not: ")
reg = re.compile("\d*\.\d+")
if re.match(reg,input_):
    print("floating no.")
else:
    print("not a floating no.") 