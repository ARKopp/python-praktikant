#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:21:01 2018

@author: Gregor
"""
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(10)
camera.stop_preview()

camera.start_preview()
sleep(5)
camera.capture("/home/pi/Desktop/image.jpg")
camera.stop_preview()

camera.start_preview()
for i in range (5):
    sleep(5)
    camera.capture("/home/pi/Desktop/python-praktikant/camera/bilder/image%s.jpg" % i)
camera.stop_preview()
