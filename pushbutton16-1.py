#!/usr/bin/env python3

#
# Filename: pushbutton16.py
# Date: 2018.08.10
# Author: Robin Greig
# Function: Turns board pin 18 off when pushbutton16 is pressed
#
import time
import os
import RPi.GPIO as GPIO

ledNum = 18
pushNum = 16

GPIO.setwarnings(False) # stop warnings from displaying
GPIO.setmode(GPIO.BOARD) # numbering scheme that represents actual pins on boards
GPIO.setup(ledNum,GPIO.OUT) # sets variable ledNum to an output
GPIO.setup(pushNum,GPIO.IN) # sets variable pushNum to an input

state = GPIO.input(pushNum)

if (state):
  GPIO.output(ledNum,GPIO.HIGH) # turn ledNum on
  print("Pin 16 is measured on")
else:
  GPIO.output(ledNum,GPIO.LOW) # turn ledNum off
  print("Pin 16 is measured off")


