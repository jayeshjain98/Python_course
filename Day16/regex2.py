# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:08:35 2019

@author: Jayesh Jain
"""
import re
input_ = """lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com"""
new = []
emails = input_.split("\n")
for email in emails: 
    if re.match(r'[a-z0-9_-]+@[a-z]+\.[a-z]+',email):
        new.append(email)
        print(new)