#!/usr/bin/env python3

#
# Filename: pushbutton16-3.py
# Date: 2018.08.10
# Author: Robin Greig
# Function: Turns board pin 18 off when pushbutton16 is pressed & introduces loop
#
from time import sleep
import os
import RPi.GPIO as GPIO

ledNum = 18
pushNum = 16

GPIO.setwarnings(False) # stop warnings from displaying
GPIO.setmode(GPIO.BOARD) # numbering scheme that represents actual pins on boards
GPIO.setup(ledNum,GPIO.OUT) # sets variable ledNum to an output
GPIO.setup(pushNum,GPIO.IN, pull_up_down=GPIO.PUD_UP) # sets variable pushNum to an input

try:
  while True: # This will continue to run until you press Ctrl-C
    state = GPIO.input(pushNum)
    if (state):
      GPIO.output(ledNum,GPIO.HIGH) # turn ledNum on
      print("Pin 16 is measured on")
    else:
      GPIO.output(ledNum,GPIO.LOW) # turn ledNum off
      print("Pin 16 is measured off")
    sleep(0.1)  # Wait 0.1 seconds

finally: # This block will run no matter how the try block exits
  GPIO.cleanup() # Clean up GPIO pins
