# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:41:31 2019

@author: Jayesh Jain
"""

def bricks_data(small_bricks, large_bricks, target):
    if target <= (small_bricks + large_bricks*5):
        return "True"
    else:
        return "False"

bricks_data(2, 2, 11)