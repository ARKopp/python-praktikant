#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 13:32:50 2018

@author: Gregor
"""

from gpiozero import Robot
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10))

for i in range(4):
    robot.forward()
    sleep(10)
    robot.right()
    sleep(1)