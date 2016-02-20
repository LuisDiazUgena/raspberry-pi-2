from time import sleep


import Image
import ImageDraw
import ImageFont

from lib_tft24T import TFT24T
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

import spidev

from subprocess import call
import commands
import os

# Raspberry Pi configuration.
#For LCD TFT SCREEN:
DC = 24
RST = 25
LED = 18

#For PEN TOUCH:
#   (nothing)

# Create TFT LCD/TOUCH object:
TFT = TFT24T(spidev.SpiDev(), GPIO, landscape=True)
# If landscape=False or omitted, display defaults to portrait mode
# This demo can work in landscape or portrait

# Initialize display.
TFT.initLCD(DC, RST, LED)
# If rst is omitted then tie rst pin to +3.3V
# If led is omitted then tie led pin to +3.3V

# Get the PIL Draw object to start drawing on the display buffer.
draw = TFT.draw()
TFT.backlite(1)
TFT.clear()
font=ImageFont.truetype('FreeSans.ttf', 50)
while True:
    temp = commands.getoutput("/opt/vc/bin/vcgencmd measure_temp")
    print temp
    try:
        temp_int = int(temp)
    except:
        print "not able to transform to int"
    if temp_int > 60:
        if TFT.is_landscape:
            draw.textwrapped((0,0), temp, 38, 20, font, "red")
        else:
            draw.textwrapped((0,0), temp, 27, 20, font, "red") # a bit narrower for portrait!
    else:
        if TFT.is_landscape:
            draw.textwrapped((0,0), temp, 38, 20, font, "lightblue")
        else:
            draw.textwrapped((0,0), temp, 27, 20, font, "lightblue") # a bit narrower for portrait!
    sleep(10)
