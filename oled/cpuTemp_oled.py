#!/usr/bin/env python

from time import sleep

import sys
from subprocess import call
import commands
import os

from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont,Image

fontName = ImageFont.truetype("font1.ttf",80)
#fontName = ImageFont.load_default()
device = ssd1306(port=1, address=0x3C)

def getTempCPU():
    temp = commands.getoutput("/opt/vc/bin/vcgencmd measure_temp")
    initTempPos = str(temp).find("=")
    finishTempPos = str(temp).find("'")
    temp = str(temp)[initTempPos+1:finishTempPos]
    try:
        temp_num = float(temp)
        return temp_num
    except:
        print "Unable to transform to float"
#Show raspberry pi logo
with canvas(device) as draw:
    logo = Image.open("pi_logo.png")
    draw.bitmap((32, 0), logo, fill=1)
    sleep(1)
#Temperature rutine
while True:
    margin = 2
    sleep_time = 2.5 #seconds

    cpuTemp = getTempCPU()

    print "Cpu Temp is:",str(cpuTemp)
    if cpuTemp and cpuTemp != oldTemp: #Just make sure the cpuTemp has a value and it's different
        with canvas(device) as draw:
            draw.text((margin,margin),str(cpuTemp),font=fontName,fill=255)
    oldTemp = cpuTemp
    sleep(sleep_time)
