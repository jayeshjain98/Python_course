# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:39:45 2019

@author: Jayesh Jain
"""
from collections import OrderedDict

od = OrderedDict()

while True:
    text = input("enter item name and value : ")
    if not text:
        break
    text1 = text.split(" ")
    price = text1[-1]
    item = " ".join(text1[:-1])
    
    
    od[item] = od.get(item,0) + int(price)



for key,value in od.items():
    print(key,value)
    

    
    