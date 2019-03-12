import urllib
import requests

url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

page = urllib.request.urlopen(url)

from bs4 import BeautifulSoup

html = BeautifulSoup(page,"lxml")

table = html.find('table',{'class':'wikitable'})

A,B,C,D,E,F = [],[],[],[],[],[]

for row in table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())

import pandas as pd
from collections import OrderedDict

col_name = ["State or UN","Admin Cap","Legis Cap","Judi Cap","Year","Capital"]

col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))

data = pd.DataFrame(col_data) 


df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=A
df['Legislative_Capital']=C
df['Judiciary_Capital']=D
df['Year_Capital']=E
df["Former_Capital"] = F
df.to_csv("former.csv")