from time import sleep

import sys
from subprocess import call
import commands
import os

from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont

font = ImageFont.load_default()
oled = ssd1306(port=1, address=0x3C)

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

with canvas(oled) as draw:
    padding = 2
    sleep_time = 2.5 #seconds

    font = ImageFont.load_default()
    while True:
        cpuTemp = getTempCPU()

        draw.text((x,x),cpuTemp,font=font,fill=255)
        sleep(sleep_time)
