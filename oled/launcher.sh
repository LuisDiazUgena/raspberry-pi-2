#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/Desktop/github-projects/raspberry-pi-2/oled
python cpuTemp_oled.py
cd /
