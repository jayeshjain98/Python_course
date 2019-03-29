# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:02:05 2019

@author: Jayesh Jain
"""

import pandas as pd
from selenium import webdriver

url = "https://en.wikipedia.org/wiki/Economy_of_India"

driver = webdriver.Chrome("C:/Users/Jayesh Jain/Downloads/chromedriver_win32/chromedriver.exe")

driver.get(url)

right_table=driver.find_element_by_class_name('wikitable')

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    
    
    if len(cells) == 7:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        G.append(cells[6].text.strip())

from collections import OrderedDict

col_name = ["Year","GDP\n(in Bil. US$ PPP)","GDP per capita\n(in US$ PPP)","Share of world\n(GDP PPP in %)","GDP growth\n(real)","Inflation rate\n(in Percent)","Government debt\n(in % of GDP)"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F,G]))
df = pd.DataFrame(col_data) 
df.to_csv("GDPgrowth.csv")






driver.quit()
        
        