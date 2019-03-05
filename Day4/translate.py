# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:16:07 2019

@author: Jayesh Jain
"""
input_str = input("enter any string ")
line_str = input_str.lower()

def translate(input_str):
    new_str = ""
    vowels = ['a','e','i','o','u',' ']
    for i in input_str:
        if i not in vowels:
            new_str = new_str + i+'o'+i
        else:
            new_str += i
    return new_str

translate(line_str)
            