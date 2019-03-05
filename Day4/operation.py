# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:29:52 2019

@author: Jayesh Jain
"""

input_length = int(input("enter length of list:"))
new_list = []
for i in range(0,input_length):
    new_input = int(input("enter element of list:"))
    new_list.append(new_input)
def addition(list_):
    a = 0
    for i in list_:
        a += i
    return a

addition(new_list)

def multiplication(list_):
    a =1
    for i in list_:
        a *= i
    return a

multiplication(new_list)

def largest(list_):
    a = 0
    for i in list_:
        if i>=a:
            a = i
        else:
            continue
    return a

largest(new_list)

def smallest(list_):
    a = list_[0]
    for i in list_:
        if i<=a:
            a = i
        else:
            continue
    return a

smallest(new_list)

def sorting(list_):
    for i in range(len(list_)):
        swapped = False
        i = 0
        while i<(len(list_)-1):
            if list_[i]>list_[i+1]:
                list_[i],list_[i+1] = list_[i+1],list_[i]
                swapped = True
            i +=1
        if swapped == False:
            break
    return list_


sorting(new_list)

def removeDuplicate(list_):
    new = []
    for i in list_:
        if i in new:
            pass
        else:
            new.append(i)
    return new

removeDuplicate(new_list)

def Print():
    print("addition=",addition(new_list))
    print("multiplication=",multiplication(new_list))
    print("largest=",largest(new_list))
    print("smallest=",smallest(new_list))
    print("sorted=",sorting(new_list))
    print("without duplicates=",removeDuplicate(new_list))

Print()
        


        
        