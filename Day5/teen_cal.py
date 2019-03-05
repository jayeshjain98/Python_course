# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 19:11:05 2019

@author: Jayesh Jain
"""

dict1 = {"a" : 2, "b" : 15, "c" : 13}
list1 = dict1.values()
print(list1)
def fix_teen(n):
    if i in [13,14,17,18,19]:
        n = 0
    else:
        n = n
    return n

sum_ = 0
for i in list1:
    sum_ += fix_teen(i)
print(sum_)

            
    
    
