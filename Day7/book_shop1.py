# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from functools import reduce 
order_summary =  [[34587, "Learning Python", "Mark Lutz",  4, 40.95],
    [98762, "Programming Python", "Mark Lutz", 5, 56.80],
    [77226, "Head First Python", "Paul Barry", 3, 32.95],
    [88112, "Einführung in Python3", "Bernd Klein",  3, 24.99]]

order_list = tuple([n.pop(0) for n in order_summary])
order_quantity = [n.pop(2) for n in order_summary]
order_price = [n.pop(2) for n in order_summary]

order_value = [a*b for a,b in zip(order_quantity,order_price)]
order_value = tuple(map(lambda x: x+10 if(x<100) else x, order_value))
summary_list = (order_list,order_value)
print(summary_list)
