#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:59:34 2018

@author: Gregor
"""

from gpiozero import TrafficLights
from time import sleep

lights = TrafficLights(2, 3, 4)

lights.green.on()

while True:
    sleep(10)
    lights.green.off()
    lights.amber.on
    sleep(1)
    lights.amber.off()
    lights.red.on
    sleep(10)
    lights.amber.on
    sleep(1)
    lights.green.on()
    lights.amber.off()
    lights.red.off
    