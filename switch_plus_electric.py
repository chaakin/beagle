import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import os
 
GPIO.setup("P8_11", GPIO.IN)
GPIO.setup("P8_14", GPIO.OUT)
GPIO.output("P8_14", GPIO.LOW)
 
old_switch_state = 0


blink_stop = 'no'


def switch():
    while True:
        new_switch_state = GPIO.input("P8_11")
        if new_switch_state == 1 and old_switch_state == 0:
            print('Running routine!')
            with open("stop_blink.txt","a+") as f:
                f.write('pause')
                f.close()

            ### Run main script
            os.system("mpg123 Electricity6.mp3")

            time.sleep(0.1)
            os.remove("stop_blink.txt")
        old_switch_state = new_switch_state

switch()


