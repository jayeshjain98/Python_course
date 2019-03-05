# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 22:11:32 2019

@author: Jayesh Jain
"""

length_arr = int(input("enter length of the array of integers:"))
input_arr = input("enter the integers in list: ").split(",")
new_list = []
for i in range(0,length_arr):
    new_list.append(int(input_arr[i]))
print(new_list)

for i in range(0,length_arr):
    if new_list[i] == 13 and i == (length_arr-1):
        new_list[i] = 0
    elif new_list[i] == 13 and i != (length_arr-1):
         new_list[i] = 0
         new_list[i+1] = 0
print(new_list)

a = 0
for i in new_list:
    a += i

print("sum count:",a)