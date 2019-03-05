# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:14:46 2019

@author: Jayesh Jain
"""


import os
os.chdir ="C:/Users/Jayesh Jain/Downloads"
from collections import Counter

def character_count(filename):
    with open(filename,"rt") as file:
        character = Counter(list(file.read()))
        count = 0
        for letter in character:
            count += 1
    return "number of characters :",count

def words_count(filename):
    with open(filename,"rt") as file:
        words = (file.read()).split(" ")
        count = 0
        for word in words:
            count += 1
    return "number of words :",count

def file_lines(filename):
    with open(filename,"rt") as file:
        count = 0
        for line in file:
            count += 1
    return "number of lines in file :",count

def unique_words(filename):
    with open(filename,"rt") as file:
        words = Counter((file.read()).split(" "))
        count = 0
        for word in words.keys():
            count += 1
    return "number of unique words :",count

def Word_count(filename):
    return character_count(filename),words_count(filename),file_lines(filename),unique_words(filename)
Word_count("romeo.txt")