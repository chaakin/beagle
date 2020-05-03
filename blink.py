import Adafruit_BBIO.GPIO as GPIO
import time
import os
 
GPIO.setup("P8_14", GPIO.OUT)  # LED in arm switch
GPIO.setup("P8_10", GPIO.OUT)  # LED hat/shocker
GPIO.output("P8_10", GPIO.LOW)

count = 0
count2 = 0

def blink(pin, btime, duration):
    for a in range(duration):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(btime)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(btime)

while True:

    if os.path.isfile('stop_blink.txt'):
        GPIO.output("P8_14", GPIO.LOW)
        GPIO.setup("P8_10", GPIO.OUT)
        GPIO.output("P8_10", GPIO.LOW)
        time.sleep(0.5)
        count = 0
        count2 = 0

    else:

        ### If we blink for more than 5mins, start playing music
        if count2 >= 30:
            blink("P8_10", 0.03, 50)
            count2 = 0

        if count >= 300:
            ps_chk = os.popen('ps ax | grep python | grep play_mp3 | grep -v grep').read()
            if 'python' in ps_chk and 'play_mp3' in ps_chk:
                print('Already playing music, skipping execution. .')
            else:
                ### Execute play_mp3.py in background if its not already running
                print('Starting to play some random music now. .')
                os.system('python play_mp3.py &')
            count = 0

        GPIO.output("P8_14", GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output("P8_14", GPIO.LOW)
        time.sleep(0.7)
        count += 1.4
        count2 += 1.4
        print('Current Count:%s' % count)
        os.system('echo "Current Counts:%s #2:%s" > /root/count.txt' % (count,count2))
