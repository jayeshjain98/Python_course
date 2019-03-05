# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:11:48 2019

@author: Jayesh Jain
"""


import os
os.chdir ="C:/Users/Jayesh Jain/Downloads"
from PIL import Image


for file in os.listdir('.'):
    if file.endswith(".png"):
        img = Image.open(file)
        width, height = img.size   # Get dimensions

        left = (width - 150)/2
        top = (height - 90)/2
        right = (width + 150)/2
        bottom = (height + 90)/2

        img = img.crop((left, top, right, bottom))
        img.save(file)