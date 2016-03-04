#!/usr/bin/env python

from time import sleep

import sys
from subprocess import call
import commands
import os

from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont

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

while True:
    margin = 2
    sleep_time = 2.5 #seconds
    with canvas(device) as draw:

        cpuTemp = getTempCPU()
        print "Cpu Temp is:",str(cpuTemp)
        if cpuTemp: #Just make sure the cpuTemp has a value
            draw.text((margin,margin),str(cpuTemp),font=fontName,fill=255)
        sleep(sleep_time)
