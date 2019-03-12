# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:40:54 2019

@author: Jayesh Jain
"""

shopping_list = []

while(True):
    input_item = input("enter new input item :")
    if input_item.upper() == "DONE":
        break
    elif input_item.upper() == "HELP":
        print("""_____INSTRUCTIONS_____
        ->use SHOW,Show,show command to see what is currently in the list
        ->use HELP,Help,help command to see all the help for these special commands
        ->use DONE,Done,done command to quit the program. """)
    elif input_item.upper() == "SHOW":
        print("items in list are :")
        for item in shopping_list:
            print(item)
    else:
        shopping_list.append(input_item)

with open("Shopping_list.txt","w") as file:
    for item in shopping_list:
        file.write(item+"\n")