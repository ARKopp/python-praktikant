# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
    

from gpiozero import LED
from time import sleep

red = LED(24)  #LED an pin 24

while True:
    red.on()
    sleep(3)
    red.off()
    sleep(3)
    