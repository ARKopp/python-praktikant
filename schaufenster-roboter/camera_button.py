#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:04:15 2018

@author: Gregor
"""

from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(21)
camera = PiCamera()

camera.start_preview()
button.wait_for_press()
camera.capture('/home/pi/image3.jpg')
camera.stop_preview()