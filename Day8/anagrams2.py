# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:56:44 2019

@author: Jayesh Jain
"""

#this approach is taking lot of time
with open('anagram.txt', 'r') as fp:
    line = fp.readlines()
dict1 = {}
for word in line:
    a = list(word)
    a.sort()
    dict1[word] = ''.join(a)
list2 = []
for value in dict1.values():
    list1 = []
    for x in dict1.items():
        if value in x:
            list1.append(x)
    list2.append(list1)
print(list2)
