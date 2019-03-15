# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:45:55 2019

@author: Jayesh Jain
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome("C:/Users/Jayesh Jain/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://www.flipkart.com/")
close_register=driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
close_register.click()
#search_engine=driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')

enter_product=driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys("iphone")

init_search=driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
init_search.click()

driver.set_page_load_timeout("15")



from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

myurl="https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"

uclient = ureq(myurl) #opens the connection
req=uclient.read()  #read the complete html page and save in variable
uclient.close()       #close the connection
 
req=soup(req,'html.parser')#html5lib
containers= req.findAll('div',{'class':'_1UoZlX'})
#print (len(containers))

#print (soup.prettify(containers[0]))
container=containers[0]

name=container.findAll('div',{'class':'_3wU53n'})
#print (name[1].text)

price=container.findAll('div',{'class':'_1vC4OE _2rQ-NK'})
#print (price[0].text)

rating=container.findAll('div',{'class':'hGSR34'})
#print (rating[0].text)

f=open("products.csv","w")
headers="name,price,ratings\n"
f.write(headers)

for container in containers:
    name=container.findAll('div',{'class':'_3wU53n'})
    name=name[0].text
    
    price=container.findAll('div',{'class':'_1vC4OE _2rQ-NK'})
    price=price[0].text
    fprice=price.replace("₹","Rs. ")
    ffprice=fprice.replace(",",".")
    rating=container.findAll('div',{'class':'hGSR34'})
    rating=rating[0].text
    fname=name.replace(",","|")    
    det= (fname + "," + ffprice + "," + rating +"\n")
    f.write(det)
    #f.write(fname+",")
    #f.write(fprice+",")
    #f.write(rating)
    
f.close()

import pandas as pd
df=pd.read_csv("products.csv")