import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time

red1 = "P8_13"
green1 = "P8_19"
blue1 = "P9_14"

red2 = "P9_42"
green2 = "P9_16"
blue2 = "P9_21"

PWM.start(red1, 0)
PWM.start(blue1, 0)
PWM.start(green1, 0)
 
PWM.start(red2, 0)
PWM.start(blue2, 0)
PWM.start(green2, 0)
 
def fade(colorA, colorB, ignore_color):
    PWM.set_duty_cycle(ignore_color, 0)
    for i in range(0, 100):
	    PWM.set_duty_cycle(colorA, 100-i)
	    PWM.set_duty_cycle(colorB, i)
	    time.sleep(0.004)

red3 = "P8_12"
green3 = "P8_14"
blue3 = "P8_16"

GPIO.setup(red3, GPIO.OUT)
GPIO.setup(green3, GPIO.OUT)
GPIO.setup(blue3, GPIO.OUT)


while True:

    fade(red1, green1, blue1)
    fade(red2, green2, blue2)
    fade(green1, blue1, red1)
    fade(green2, blue2, red2)
    fade(blue1, red1, green1)
    fade(blue2, red2, green2)
    fade(red1, green1, blue1)
    fade(red2, green2, blue2)
    fade(green1, blue1, red1)
    fade(green2, blue2, red2)
    fade(blue1, red1, green1)
    fade(blue2, red2, green2)
    fade(red1, green1, blue1)
    fade(red2, green2, blue2)
    fade(green1, blue1, red1)
    fade(green2, blue2, red2)
    fade(blue1, red1, green1)
    fade(blue2, red2, green2)
    fade(red1, green1, blue1)
    fade(red2, green2, blue2)
    fade(green1, blue1, red1)
    fade(green2, blue2, red2)
    fade(blue1, red1, green1)
    fade(blue2, red2, green2)

    for i in range(4):
        iNew = str(i)
        iNew = '0.'+iNew
        iNew = float(iNew)
        GPIO.output(red3, GPIO.HIGH)
        GPIO.output(green3, GPIO.LOW)
        GPIO.output(blue3, GPIO.LOW)
        time.sleep(iNew)
        GPIO.output(red3, GPIO.HIGH)
        GPIO.output(green3, GPIO.HIGH)
        GPIO.output(blue3, GPIO.LOW)
        time.sleep(iNew)
        GPIO.output(red3, GPIO.LOW)
        GPIO.output(green3, GPIO.HIGH)
        GPIO.output(blue3, GPIO.LOW)
        time.sleep(iNew)
        GPIO.output(red3, GPIO.LOW)
        GPIO.output(green3, GPIO.HIGH)
        GPIO.output(blue3, GPIO.HIGH)
        time.sleep(iNew)
        GPIO.output(red3, GPIO.LOW)
        GPIO.output(green3, GPIO.LOW)
        GPIO.output(blue3, GPIO.HIGH)
        time.sleep(iNew)
        GPIO.output(red3, GPIO.HIGH)
        GPIO.output(green3, GPIO.LOW)
        GPIO.output(blue3, GPIO.HIGH)
        time.sleep(iNew)
        GPIO.output(red3, GPIO.HIGH)
        GPIO.output(green3, GPIO.HIGH)
        GPIO.output(blue3, GPIO.HIGH)
        time.sleep(iNew)
        GPIO.output(red3, GPIO.LOW)
        GPIO.output(green3, GPIO.LOW)
        GPIO.output(blue3, GPIO.LOW)
        time.sleep(iNew)



print 'blinking complete!'
