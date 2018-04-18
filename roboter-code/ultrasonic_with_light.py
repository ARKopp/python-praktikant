#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 12:52:21 2018

@author: Gregor
"""

from gpiozero import DistanceSensor, LED
from signal import pause

sensor = DistanceSensor(17, 18 max_distance=1, treshold_distance=0.2)
led = LED(13)

sensor.when_in_range = led.on
sensor.when_out_of_range = led.off

pause()