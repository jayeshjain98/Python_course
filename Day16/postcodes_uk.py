# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:36:38 2019

@author: Jayesh Jain
"""
import os
os.chdir("C:/Users/Jayesh Jain/Downloads/python files")
import re
example_codes = ["SW1A 0AA", # House of Commons
                 "SW1A 1AA", # Buckingham Palace
                 "SW1A 2AA", # Downing Street
                 "BX3 2BB", # Barclays Bank
                 "DH98 1BT", # British Telecom
                 "N1 9GU", # Guardian Newspaper
                 "E98 1TT", # The Times
                 "TIM E22", # a fake postcode
                 "A B1 A22", # not a valid postcode
                 "EC2N 2DB", # Deutsche Bank
                 "SE9 2UG", # University of Greenwhich
                 "N1 0UY", # Islington, London
                 "EC1V 8DS", # Clerkenwell, London
                 "WC1X 9DT", # WC1X 9DT
                 "B42 1LG", # Birmingham
                 "B28 9AD", # Birmingham
                 "W12 7RJ", # London, BBC News Centre
                 "BBC 007" # a fake postcode
                ]
with open("validpostcodes.txt","wt") as file:
    
    for code in example_codes:
        if re.match(r'[A-Z]{1,2}R?(\d[A-Z]|\d{2}|\d)\ [0-9][QWERTYUPASDFGHJLZXBN]{2}',code):
            print(code,",it is a valid code\n")
            file.write(code)
        else:
            print(code,",it is not a valid code\n")