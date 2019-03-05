# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:00:13 2019

@author: Jayesh Jain
"""

import os
os.chdir ="C:/Users/Jayesh Jain/Downloads"

from PIL import Image

filename = input("enter file name with extension :")

img = Image.open(filename)

width, height = img.size   # Get dimensions

left = (width - 150)/2
top = (height - 90)/2
right = (width + 150)/2
bottom = (height + 90)/2

img = img.crop((left, top, right, bottom))
img = img.convert('LA')
img = img.rotate(270)
img.save("greyscale.png")

#im = Image.open(filename)
#im = im.thumbnail((128, 128), Image.ANTIALIAS)

#im.save("greyscales.png JPEG")
import glob

# get all the jpg files from the current folder
for infile in glob.glob("*.jpg"):
  im = Image.open(infile)
  # convert to thumbnail image
  im.thumbnail((128, 128), Image.ANTIALIAS)
  # don't save if thumbnail already exists
  if infile[0:2] != "T_":
    # prefix thumbnail file with T_
    im.save("T_" + infile, "JPEG")
