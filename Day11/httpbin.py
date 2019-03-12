# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:19:32 2019

@author: Jayesh Jain
"""


import requests
import json

Host = "http://httpbin.org/post"

data ={"firstname":"Chris","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response.text

print ( post_method() )

def get_method():
    response = requests.get("http://httpbin.org/get?firstname=Chris&language=English")
    return response.text

print (get_method())

