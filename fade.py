import Adafruit_BBIO.PWM as PWM
import time
 
red = "P8_13"
green = "P8_19"
blue = "P9_14"
 
PWM.start(red, 0)
PWM.start(blue, 0)
PWM.start(green, 0)
 
def fade(colorA, colorB, ignore_color):
    PWM.set_duty_cycle(ignore_color, 0)
    for i in range(0, 100):
	    PWM.set_duty_cycle(colorA, 100-i)
	    PWM.set_duty_cycle(colorB, i)
	    time.sleep(0.001)
	
while True:
    fade(red, green, blue)
    fade(green, blue, red)
    fade(blue, red, green)
