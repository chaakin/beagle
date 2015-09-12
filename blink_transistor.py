import Adafruit_BBIO.GPIO as GPIO
import time

#GPIO.setup("P9_12", GPIO.OUT)
GPIO.setup("P8_12", GPIO.OUT)


def Blink(numTimes,speed):
    for i in range(0,numTimes):## Run loop numTimes

#        GPIO.output("P9_12", GPIO.HIGH)## Switch on pin 7
        GPIO.output("P8_12", GPIO.HIGH)## Switch on pin 7
        time.sleep(speed)## Wait
#        GPIO.output("P9_12", GPIO.LOW)## Switch off pin 7\
        GPIO.output("P8_12", GPIO.LOW)## Switch off pin 7
        time.sleep(speed)## Wait

 
## Ask user for total number of blinks and length of each blink
#iterations = input("Enter total number of times to blink: ")
speed = input("Enter length of each blink(seconds): ")
 
## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
Blink(100000,float(speed))


