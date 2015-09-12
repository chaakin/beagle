import Adafruit_BBIO.GPIO as GPIO
import time
import os
 
GPIO.setup("P8_12", GPIO.OUT)


### Run main script

# Blink ambient lights a few times for effect?
GPIO.output("P8_12", GPIO.HIGH)
time.sleep(.5)
GPIO.output("P8_12", GPIO.LOW)
time.sleep(.5)
GPIO.output("P8_12", GPIO.HIGH)
time.sleep(.5)
GPIO.output("P8_12", GPIO.LOW)
time.sleep(.5)

# Turn off ambient lights
GPIO.output("P8_12", GPIO.HIGH)

os.system("mpg123 Electricity6.mp3 &")
os.system("python electric_blink.py")

# Turn on ambient lights
GPIO.output("P8_12", GPIO.LOW)
