#!/usr/bin/env python3
"""
'digital_in-status.py'
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
ADAFRUIT_IO_KEY = '40f32646af2e4476a94440107ed48a19'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'Chandra723'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we have a 'test' feed
    test = aio.feeds('test')
    digital = aio.feeds('digital')
except RequestError: # create a digital feed
    feed = Feed(name="test")
    test = aio.create_feed(feed)

# button set up
button = digitalio.DigitalInOut(board.D23)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_current = 0

# led set up
led = digitalio.DigitalInOut(board.D24)
led.direction = digitalio.Direction.OUTPUT


while True:
    if not button.value:
        button_current = 1
    else:
        button_current = 0

    print('Button -> ', button_current)
    aio.send(test.key, button_current)
    aio.send(digital.key, button_current)

    # set the LED to the feed value
    led.value = abs(button_current-1)


    # avoid timeout from adafruit io
    time.sleep(1)
