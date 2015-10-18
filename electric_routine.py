import Adafruit_BBIO.GPIO as GPIO
import time
import os
 
GPIO.setup("P8_12", GPIO.OUT)


### Run main script

# Blink ambient lights a few times for effect?
GPIO.output("P8_12", GPIO.HIGH)
time.sleep(.7)
GPIO.output("P8_12", GPIO.LOW)
time.sleep(.7)

# Turn off ambient lights
GPIO.output("P8_12", GPIO.HIGH)
time.sleep(.7)
os.system("mpg321 Percy_Roll2.mp3")
time.sleep(.7)

os.system("mpg321 Electricity6.mp3 &")
os.system("python electric_blink.py")

# Turn on ambient lights
time.sleep(2)
GPIO.output("P8_12", GPIO.LOW)
