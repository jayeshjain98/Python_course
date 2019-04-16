# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 17:09:25 2019

@author: Jayesh Jain
"""

class Radio:
    def __init__(self, height, width, length, brandname, colour, antenna, power, vol, freq):
        self.height = height
        self.width = width
        self.length = length
        self.brandname = brandname
        self.colour = colour
        self.antenna = antenna
        self.power = power
        self.statusled = power
        self.vol = vol
        self.freq = freq
        
    def on_off_switch(self,power):
        self.statusled = power
        
    def volume(self,vol):
        self.vol = vol
        
    def tuner(self,a):
        self.freq = a
    
    
radio = Radio(8.5, 4.5, 11.5, "Jainson", "black", True, True, 7, 93.5) 

radio.freq
radio.tuner(23.6)

class FM( Radio ):
    def __init__(self, height, width, length, brandname, colour, antenna, power, vol, freq, channel):
        super().__init__(height, width, length, brandname, colour, antenna, power, vol, freq)
        self.channel = channel
    def set_channel(self, a):
        self.channel = a

fm = FM(8.5, 4.5, 11.5, "Jainson", "black", True, True, 7, 93.5, "FM Tadka")
name = "Radio Mirchi"
fm.set_channel(name) 
fm.channel
    