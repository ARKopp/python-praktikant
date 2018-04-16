#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 15:29:41 2018

@author: Gregor
"""


from gpiozero import Robot
from time import sleep

robot = Robot(left=(10, 9)), right=(7, 8)

while True:
    robot.forward()
    sleep(5)
    robot.stop()
    sleep(5)
    
    