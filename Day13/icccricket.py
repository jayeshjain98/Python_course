# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:02:57 2019

@author: Jayesh Jain
"""

from bs4 import BeautifulSoup
import requests


url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(url).text
soup = BeautifulSoup(source)

right_table=soup.find('table', class_='table')

A,B,C,D,E = [],[],[],[],[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    if len(cells)==5:
        A.append(int(cells[0].find(text=True)))
        B.append(str(cells[1].find(text=True)))
        C.append(int(cells[2].find(text=True)))
        D.append(str(cells[3].find(text=True)))
        E.append(int(cells[4].find(text=True)))
        
import pandas as pd
df=pd.DataFrame(A,columns=['Ranking'])
df['Country'] = B
df['Weighted Matches'] = C
df['Points'] = D
df["Rating"] = E

df.to_csv("icc_rating.csv")