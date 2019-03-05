# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 23:58:35 2019

@author: Jayesh Jain
"""

import string
alphabets = string.ascii_lowercase
user_input = input("enter string : ").lower()
count = 0
index = 0
for letter in user_input:
    if letter in alphabets:
        count += 1
    elif letter in "1234567890":
        index += 1
print("Letters",count)
print("Digits",index)


