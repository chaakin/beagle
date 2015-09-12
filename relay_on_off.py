import Adafruit_BBIO.GPIO as GPIO
import time
import os
 
GPIO.setup("P8_12", GPIO.OUT)


while True:

    GPIO.output("P8_12", GPIO.HIGH)
    time.sleep(5)
    GPIO.output("P8_12", GPIO.LOW)
    time.sleep(5)

