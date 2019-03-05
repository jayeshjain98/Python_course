# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:01:32 2019

@author: Jayesh Jain
"""

input_str = input("enter your name ")
length = len(input_str)
index_ = input_str.index(" ")
print(index_)
print(input_str[slice(index_ + 1,length)],input_str[slice(index_)])



