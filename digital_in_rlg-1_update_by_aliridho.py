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
ADAFRUIT_IO_KEY = 'cccb172c5c534687ad188bea38b1695c'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'barakbah'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we have a 'digital' feed
    digital = aio.feeds('doorstate')
except RequestError: # create a digital feed
    feed = Feed(name="doorstate")
    doorstate = aio.create_feed(feed)

# button set up
button = digitalio.DigitalInOut(board.D23)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_current = 0

counter=0;
while True:
    if not button.value:
        button_current = 1
        counter=counter+10
    else:
        button_current = 0
        counter=counter-10
    
    if (counter>100):
        counter=100
    if (counter<0):
        counter=0


    print('Button -> ', button_current)
    aio.send(digital.key, counter)

    # avoid timeout from adafruit io
    time.sleep(1)
