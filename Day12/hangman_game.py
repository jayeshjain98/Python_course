# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:27:28 2019

@author: Jayesh Jain
"""

import random


file = open("Fruits.txt","r")
content = file.read()
fruits = content.split("\n")
            

word = random.choice(fruits)

z=word
counter = 0
while(True):
    input_letter = input("enter your best guess :")
    if not input_letter:
        print("you quit the game")
        break
    
    if input_letter in word:
        a = list(word)
        a.pop(a.index(input_letter))
        word = "".join(a)
        print("letter in word")
        if word == "":
            print("you win")
    else:
        print("letter not in word")
        counter += 1
        if counter>3:
            print("yon lose! Word is :",z)
            break
        