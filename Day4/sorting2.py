# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
new_list = []

while True:
    user_input = input("enter data : ")
    x = ''
    if not user_input:
        break
    
    name,age,score = user_input.split(",")
    new_list.append((name,int(age),int(score)))

new_list.sort()
print(new_list)