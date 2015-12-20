import Adafruit_BBIO.GPIO as GPIO
import time
import os
 
GPIO.setup("P8_11", GPIO.IN)

# Make sure main LEDs are off!
GPIO.setup("P8_10", GPIO.OUT)
GPIO.output("P8_10", GPIO.LOW)
 
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

            ### Kill any music that may be playing
            pm_pid = os.popen("ps ax | grep python | grep play_mp3 | grep -v grep | awk '{print $1}'").read()
            os.system('kill -9 %s' % pm_pid)
            os.system('killall mpg321')
            time.sleep(1)

            os.system("mpg321 Percy_Have_Mercy.mp3")

            ### Run main script
            os.system("python electric_routine.py")

            time.sleep(0.1)
            os.remove("stop_blink.txt")
        old_switch_state = new_switch_state

switch()


