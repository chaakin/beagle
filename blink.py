import Adafruit_BBIO.GPIO as GPIO
import time
import os
 
GPIO.setup("P8_14", GPIO.OUT)


while True:

    if os.path.isfile('stop_blink.txt'):
        GPIO.output("P8_14", GPIO.LOW)
        time.sleep(0.5)

    else:
        GPIO.output("P8_14", GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output("P8_14", GPIO.LOW)
        time.sleep(0.5)

