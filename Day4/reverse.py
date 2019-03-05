# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:51:56 2019

@author: Jayesh Jain
"""

def reverse_string(line_str):
    length_str = len(line_str)
    new_str = ""
    while length_str >= 0:
        new_str += line_str[length_str-1]
        length_str -= 1
    return new_str
name = input("enter string")

reverse_string(name)
        