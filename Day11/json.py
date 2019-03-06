# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:21:26 2019

@author: Jayesh Jain
"""

import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
response = requests.get(url)
print(response.text)

jsondata = response.json()

print("logitude :",jsondata["coord"]["lon"])
print("latitude :",jsondata["coord"]["lat"])
print("Weather Condition :",jsondata["weather"][0]["description"])
print("Wind Speed :",jsondata["wind"]["speed"])
print("sunset :",jsondata["sys"]["sunset"])
print("sunrise :",jsondata["sys"]["sunrise"])


on



