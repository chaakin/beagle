import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import os
 
GPIO.setup("P8_12", GPIO.IN)
GPIO.setup("P8_10", GPIO.OUT)
GPIO.output("P8_10", GPIO.LOW)
 
old_switch_state = 0


red1 = "P8_13"
red2 = "P8_19"
red3 = "P9_14"
red4 = "P9_42"
red5 = "P9_16"
red6 = "P9_21"
red7 = "P9_22"
red8 = "P9_28"

# Start PWM on Red
PWM.start(red1, 100)
PWM.start(red2, 100)
PWM.start(red3, 100)
PWM.start(red4, 100)
PWM.start(red5, 100)
PWM.start(red6, 100)
PWM.start(red7, 100)
PWM.start(red8, 100)

PWM.start(red1, 0)
PWM.start(red2, 0)
PWM.start(red3, 0)
PWM.start(red4, 0)
PWM.start(red5, 0)
PWM.start(red6, 0)
PWM.start(red7, 0)
PWM.start(red8, 0)

blink_stop = 'no'


def switch():
    while True:
        new_switch_state = GPIO.input("P8_12")
        if new_switch_state == 1 and old_switch_state == 0:
            print('Running routine!')
            with open("stop_blink.txt","a+") as f:
                f.write('pause')
                f.close()

            ### Run main script
            os.system("mpg123 Electricity4.mp3 &")
            os.system("python red_fade_routine.py")

            time.sleep(0.1)
            os.remove("stop_blink.txt")
        old_switch_state = new_switch_state

switch()


