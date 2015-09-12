import Adafruit_BBIO.PWM as PWM
import time
 
red1 = "P8_13"
green1 = "P8_19"
blue1 = "P9_14"


PWM.start(red1, 100)
PWM.start(blue1, 100)
PWM.start(green1, 100)
 
 
def fade(colorA, colorB, ignore_color):
    PWM.set_duty_cycle(ignore_color, 0)
    for i in range(0, 100):
	    PWM.set_duty_cycle(colorA, 100-i)
	    PWM.set_duty_cycle(colorB, i)
	    time.sleep(0.004)

try:	
    while True:
        fade(green1, blue1, red1)
        fade(blue1, red1, green1)
        fade(red1, green1, blue1)


except KeyboardInterrupt:
    PWM.start(red1, 100)
    PWM.start(green1, 100)
    PWM.start(blue1, 100)

