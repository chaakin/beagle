import Adafruit_BBIO.GPIO as GPIO
import time
import os
 
GPIO.setup("P8_10", GPIO.OUT)


def blink(pin, btime, duration):
    for a in range(duration):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(btime)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(btime)



blink("P8_10", 0.03, 17)
time.sleep(0.5)


blink("P8_10", 0.03, 50)
time.sleep(1)


blink("P8_10", 0.03, 115)

