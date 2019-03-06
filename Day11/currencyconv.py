# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:50:33 2019

@author: Jayesh Jain
"""


import requests

url1 = "http://free.currencyconverterapi.com/api/v5/convert"
url2 = "?q=USD_INR&compact=y"
url3 = "&apiKey=82d0883ca8073099db41"

url = url1 + url2 + url3
response = requests.get(url)
print(response.text)

jsondata = response.json()

print("Value of 1 US Dollar in Indian Rupee :",jsondata["USD_INR"]["val"])