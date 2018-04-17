#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:58:57 2018

@author: Gregor
"""

from time import sleep
from gpiozero import LED

red = LED(24)

while True:
    red on()
    sleep(1)
    red.off()
    sleep(1)
    