# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:28:02 2019

@author: Jayesh Jain
"""

import json

with open("student.json") as file:
    data = json.load(file)
print(data["Student"]["Co-curricular"][0])

