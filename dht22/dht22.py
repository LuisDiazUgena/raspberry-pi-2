#!/usr/bin/python
import Adafruit_DHT
import threading

sensor = Adafruit_DHT.DHT22
pin=21

def dht():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
    	print 'Temp={0:0.1f}C  Humidity={1:0.1f}%'.format(temperature, humidity)
    else:
    	print 'Failed to get reading. Try again!'
    threading.Timer(2.5, f).start()

dht()
