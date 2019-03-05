# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:44:21 2019

@author: Jayesh Jain
"""

length_arr = int(input("enter length of the array of integers:"))
input_arr = input("enter the integers in list: ").split(",")
new_list = []
for i in range(0,length_arr):
    new_list.append(int(input_arr[i]))

new_list.sort()
print(new_list)
del new_list[0]
del new_list[-1]
print(new_list)
a = 0
for i in new_list:
    a = a+i
mean = a/len(new_list)
print("mean average of the values is: ",mean)
    