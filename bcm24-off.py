#!/usr/bin/env python3

#
# Filename: bcm24-off.py
# Date: 2018.08.10
# Author: Robin Greig
# Function: Turns gpio pin 24 off
#
import time
import os
import RPi.GPIO as GPIO

pinNum = 24

GPIO.setwarnings(False) # stop warnings from displaying
GPIO.setmode(GPIO.BCM) # numbering scheme that represents breakout boards & pin layout
GPIO.setup(pinNum,GPIO.OUT) # sets variable pinNum to an output

GPIO.output(pinNum,GPIO.LOW) # turn pinNum off


