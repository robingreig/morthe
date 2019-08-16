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
ADAFRUIT_IO_KEY = '8366492aadd0407393eb422252ac8be8'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'anombesari'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we have a 'digital' feed
    digital = aio.feeds('doorstate')
except RequestError: # create a digital feed
    feed = Feed(name="doorstate")
    doorstate = aio.create_feed(feed)

# button set up
button1 = digitalio.DigitalInOut(board.D23)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D25)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

val = 0

while True:
    if not button1.value:
        val = val + 1
          
    if not button2.value:
        val = val - 1

    print('Value -> ', val)
    aio.send(digital.key, val)

    # avoid timeout from adafruit io
    time.sleep(2)
