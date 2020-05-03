import Adafruit_BBIO.GPIO as GPIO
import time
import os
 
GPIO.setup("P8_10", GPIO.OUT)  # LED hat/shocker
GPIO.setup("P8_15", GPIO.OUT)  # Old vibration switch
GPIO.output("P8_15", GPIO.LOW)
#GPIO.setup("P8_17", GPIO.OUT)  # Smoke machine
#GPIO.output("P8_17", GPIO.LOW)


def blink(pin, btime, duration):
    for a in range(duration):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(btime)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(btime)


#GPIO.output("P8_17", GPIO.HIGH)
#GPIO.output("P8_15", GPIO.HIGH)
blink("P8_10", 0.03, 17)
#GPIO.output("P8_15", GPIO.LOW)

time.sleep(0.5)


#GPIO.output("P8_15", GPIO.HIGH)
blink("P8_10", 0.03, 50)
#GPIO.output("P8_15", GPIO.LOW)
#GPIO.output("P8_17", GPIO.LOW)
time.sleep(1)

#GPIO.output("P8_17", GPIO.HIGH)
#GPIO.output("P8_15", GPIO.HIGH)
blink("P8_10", 0.03, 115)
#GPIO.output("P8_15", GPIO.LOW)
GPIO.output("P8_17", GPIO.LOW)

