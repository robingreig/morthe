#!/usr/bin/env python3

#
# Filename: board18-on-clean.py
# Date: 2018.08.16
# Author: Robin Greig
# Function: Turns board pin 18 on & demonstrates GPIO.cleanup()
#
import time
import os
import RPi.GPIO as GPIO

pinNum = 18

GPIO.setwarnings(False) # stop warnings from displaying
GPIO.setmode(GPIO.BOARD) # numbering scheme that represents actual pins on boards
GPIO.setup(pinNum,GPIO.OUT) # sets variable pinNum to an output

GPIO.output(pinNum,GPIO.HIGH) # turn pinNum on

time.sleep(1)
GPIO.cleanup()
