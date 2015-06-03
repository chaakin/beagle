import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P8_10", GPIO.OUT)
GPIO.setup("P8_9", GPIO.OUT)
GPIO.setup("P9_12", GPIO.OUT)


for i in range(40):
    iNew = str(i)
    iNew = '0.0'+iNew
    iNew = float(iNew)
    GPIO.output("P8_10", GPIO.HIGH)
    GPIO.output("P8_9", GPIO.HIGH)
    GPIO.output("P9_12", GPIO.HIGH)
    time.sleep(iNew)
    GPIO.output("P9_12", GPIO.LOW)
    GPIO.output("P8_9", GPIO.LOW)
    GPIO.output("P8_10", GPIO.LOW)
    time.sleep(iNew)

    GPIO.output("P8_10", GPIO.HIGH)
    GPIO.output("P8_9", GPIO.HIGH)
    GPIO.output("P9_12", GPIO.HIGH)


print 'blinking complete!'
