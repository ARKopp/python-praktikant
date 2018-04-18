#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 12:39:59 2018

@author: Gregor
"""

from gpiozero import DistanceSensor
from time import sleep 

sensor = DistanceSensor(17, 18)

while True:
    print("Distance to nearest object is", sensor.distance, "m")
    sleep(1)