#!/usr/bin/env python3

#
# Filename: pushbutton16.py
# Date: 2018.08.10
# Author: Robin Greig
# Function: Turns board pin 18 off when pushbutton16 is pressed
#
from time import sleep
import os
import sys
import RPi.GPIO as GPIO

ledNum = 18
ledNum2 = 7;
pushNum = 16

GPIO.setwarnings(False) # stop warnings from displaying
GPIO.setmode(GPIO.BOARD) # numbering scheme that represents actual pins on boards
GPIO.setup(ledNum,GPIO.OUT) # sets variable ledNum to an output
GPIO.setup(ledNum2,GPIO.OUT)
GPIO.setup(pushNum,GPIO.IN, pull_up_down=GPIO.PUD_UP) # sets variable pushNum to an input

toggle=1;
status=1;
counter=0;
while True:
  state = GPIO.input(pushNum)
  if (state==0): 
    toggle=0;
    counter=counter+1;
  
  if (state==1):
    counter=0;
  
  if ((state==1) and (toggle==0)):
    status=status+1;
    toggle=1;
    if (status>4):
      status=1;
  
  if (counter==10):
    GPIO.output(ledNum,GPIO.HIGH)
    GPIO.output(ledNum2,GPIO.HIGH)
    GPIO.cleanup()
    sys.exit(0)
  
  if (status==1):
    GPIO.output(ledNum,GPIO.HIGH) 
    GPIO.output(ledNum2,GPIO.HIGH)
  elif (status==2):
    GPIO.output(ledNum,GPIO.HIGH) 
    GPIO.output(ledNum2,GPIO.LOW)
  elif (status==3):
    GPIO.output(ledNum,GPIO.LOW) 
    GPIO.output(ledNum2,GPIO.HIGH)
  else:
    GPIO.output(ledNum,GPIO.LOW) 
    GPIO.output(ledNum2,GPIO.LOW) 
  
    
  sleep(0.1) 

