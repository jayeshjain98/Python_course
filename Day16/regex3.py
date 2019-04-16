# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:52:29 2019

@author: Jayesh Jain
"""

import re 
cards_no = """4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367 -8912-3456
5123 - 3567 - 8912 - 3456"""

cards = cards_no.split("\n")

for card in cards:
    if re.match(r'^(4|5|6)\d{3}(\-?\d{4}){3}',card):
        print("Valid")
    else:
        print("Invalid")