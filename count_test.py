import time
import os

count = 0
while True:

    if os.path.isfile('stop_blink.txt'):
#        GPIO.output("P8_14", GPIO.LOW)
        print('LOW')
        time.sleep(0.5)
        count = 0

    else:

        ### If we blink for more than 5mins, start playing music
        if count >= 30:
            ps_chk = os.popen('ps ax | grep python | grep play_mp3 | grep -v grep').read()
            if 'python' in ps_chk and 'play_mp3' in ps_chk:
                print('Already playing music, skipping execution. .')
            else:
                ### Execute play_mp3.py in background if its not already running
                print('Starting to play some random music now. .')

            count = 0
        
#        GPIO.output("P8_14", GPIO.HIGH)
        print('HIGH')
        time.sleep(0.7)
#        GPIO.output("P8_14", GPIO.LOW)
        print('LOW')
        time.sleep(0.7)

        count += 1.4
        print('Current Count:%s' % count)
