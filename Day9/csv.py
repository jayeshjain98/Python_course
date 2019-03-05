# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:12:39 2019

@author: Jayesh Jain
"""

import csv

csv_list = []
with open("passwd") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=":")
    for row in csv_reader:
        if row[0] == "#":
            pass
        else:
            csv_list.append([row[0],row[2]])

with open('output.csv', mode='w') as file:
    employee_writer = csv.writer(file, delimiter='\t')
    for entry in csv_list:
        employee_writer.writerow(entry)
    
with open('output.csv', mode='r') as file:
    print(file.read())
    
        

