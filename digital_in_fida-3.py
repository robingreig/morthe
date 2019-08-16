#!/usr/bin/env python3
"""
'digital_in.py'
==================================
Example of sending button values
to an Adafruit IO feed.

Author(s): Brent Rubell, Todd Treece
"""
# Import standard python modules
import time

# import Adafruit Blinka
import board
import digitalio

# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = '224da3c19c424fffbc140263306b60cd'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'mkmufida'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we have a 'digital' feed
    digital = aio.feeds('monitor')
except RequestError: # create a digital feed
    feed = Feed(name="monitor")
    doorstate = aio.create_feed(feed)

# button set up
button = digitalio.DigitalInOut(board.D23)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
#seetting for current button button state
button_current = 0

#to measure how long the button has been pushed
counter= 0

while True:
        
    if not button.value:
        button_current = 1
        counter=counter+5
    else:
        button_current = 0
        counter=counter-5
        
    if (counter>20):
        counter=20
    if (counter<0):
        counter=0
    
    
    #if not button.value:
    #    button_current = 1
    #else:
    #    button_current = 0

    print('Button -> ', button_current )
    aio.send(digital.key, counter)

    # avoid timeout from adafruit io
    time.sleep(2)
