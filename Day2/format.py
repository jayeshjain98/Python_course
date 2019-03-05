# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:51:31 2019

@author: Jayesh Jain
"""

input_str = """   This is a multi line string. This code challenge is to
    test your understanding about strings.
    You need to print some part of this string.
    From here print this text without manually counting the indexes."""
    
get_index = input_str.index("From")
print(input_str[get_index:])