# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:50:02 2019

@author: Jayesh Jain
"""
import string
dir(str)
help(str.replace)
input_str = "RESTART"
new_str = input_str[::-1].replace("R","$",1)
output_str = new_str[::-1]
print(output_str)