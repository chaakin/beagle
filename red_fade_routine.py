import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time


red1 = "P8_13"
red2 = "P8_19"
red3 = "P9_14"
red4 = "P9_42"
red5 = "P9_16"
red6 = "P9_21"
red7 = "P9_22"
red8 = "P9_28"

### Setup Motor/Relay GPIO
GPIO.setup("P9_41", GPIO.OUT)
GPIO.setup("P9_41", GPIO.LOW)

#pink1 = [red1,blue1]
#cyan1 = [green1,blue1]
#amber1 = [red1,green1]
#white1 = [red1,blue1,green1]

# Start PWM on Red
PWM.start(red1, 100)
PWM.start(red2, 100)
PWM.start(red3, 100)
PWM.start(red4, 100)
PWM.start(red5, 100)
PWM.start(red6, 100)
PWM.start(red7, 100)
PWM.start(red8, 100)


a = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


def fadeIn(color, speed):
    for h in reversed(range(101)):
        PWM.set_duty_cycle(color, h)
        time.sleep(speed)

def fadeOut(color, speed):
    for i in range(101):
        PWM.set_duty_cycle(color, i)
        time.sleep(speed)



for k in range(2):
    # Run right
    fadeIn(red1, 0.0002)
    fadeIn(red2, 0.0002)
    fadeOut(red1, 0.0002)
    fadeIn(red3, 0.0002)
    fadeOut(red2, 0.0002)
    fadeIn(red4, 0.0002)
    fadeOut(red3, 0.0002)
    fadeIn(red5, 0.0002)
    fadeOut(red4, 0.0002)
    fadeIn(red6, 0.0002)
    fadeOut(red5, 0.0002)
    fadeIn(red7, 0.0002)
    fadeOut(red6, 0.0002)
    fadeIn(red8, 0.0002)
    fadeOut(red7, 0.0002)
    fadeOut(red8, 0.0002)

    # Run left
    fadeIn(red8, 0.0002)
    fadeIn(red7, 0.0002)
    fadeOut(red8, 0.0002)
    fadeIn(red6, 0.0002)
    fadeOut(red7, 0.0002)
    fadeIn(red5, 0.0002)
    fadeOut(red6, 0.0002)
    fadeIn(red4, 0.0002)
    fadeOut(red5, 0.0002)
    fadeIn(red3, 0.0002)
    fadeOut(red4, 0.0002)
    fadeIn(red2, 0.0002)
    fadeOut(red3, 0.0002)
    fadeIn(red1, 0.0002)
    fadeOut(red2, 0.0002)
    fadeOut(red1, 0.0002)


    # Pause
    time.sleep(0.3)



time.sleep(0.5)

GPIO.setup("P9_41", GPIO.HIGH)

# Now blink 3 times
for j in range(2):
    PWM.set_duty_cycle(red1, 0)
    PWM.set_duty_cycle(red2, 0)
    PWM.set_duty_cycle(red3, 0)
    PWM.set_duty_cycle(red4, 0)
    PWM.set_duty_cycle(red5, 0)
    PWM.set_duty_cycle(red6, 0)
    PWM.set_duty_cycle(red7, 0)
    PWM.set_duty_cycle(red8, 0)

    time.sleep(0.3)
    PWM.set_duty_cycle(red8, 100)
    PWM.set_duty_cycle(red7, 100)
    PWM.set_duty_cycle(red6, 100)
    PWM.set_duty_cycle(red5, 100)
    PWM.set_duty_cycle(red4, 100)
    PWM.set_duty_cycle(red3, 100)
    PWM.set_duty_cycle(red2, 100)
    PWM.set_duty_cycle(red1, 100)
    time.sleep(0.3)

GPIO.setup("P9_41", GPIO.LOW)

for l in range(2):
    fadeIn(red1, 0.0002)
    time.sleep(0.0005)
    fadeIn(red2, 0.0002)
    time.sleep(0.0005)
    fadeIn(red3, 0.0002)
    time.sleep(0.0005)
    fadeIn(red4, 0.0002)
    time.sleep(0.0005)
    fadeIn(red5, 0.0002)
    time.sleep(0.0005)
    fadeIn(red6, 0.0002)
    time.sleep(0.0005)
    fadeIn(red7, 0.0002)
    time.sleep(0.0005)
    fadeIn(red8, 0.0002)

    time.sleep(0.3)

    fadeOut(red8, 0.0002)
    time.sleep(0.0005)
    fadeOut(red7, 0.0002)
    time.sleep(0.0005)
    fadeOut(red6, 0.0002)
    time.sleep(0.0005)
    fadeOut(red5, 0.0002)
    time.sleep(0.0005)
    fadeOut(red4, 0.0002)
    time.sleep(0.0005)
    fadeOut(red3, 0.0002)
    time.sleep(0.0005)
    fadeOut(red2, 0.0002)
    time.sleep(0.0005)
    fadeOut(red1, 0.0002)
    time.sleep(0.0005)


GPIO.setup("P9_41", GPIO.HIGH)

for m in range(2):
    fadeIn(red8, 0.0002)
    time.sleep(0.0005)
    fadeIn(red7, 0.0002)
    time.sleep(0.0005)
    fadeIn(red6, 0.0002)
    time.sleep(0.0005)
    fadeIn(red5, 0.0002)
    time.sleep(0.0005)
    fadeIn(red4, 0.0002)
    time.sleep(0.0005)
    fadeIn(red3, 0.0002)
    time.sleep(0.0005)
    fadeIn(red2, 0.0002)
    time.sleep(0.0005)
    fadeIn(red1, 0.0002)

    time.sleep(0.3)

    fadeOut(red1, 0.0002)
    time.sleep(0.0005)
    fadeOut(red2, 0.0002)
    time.sleep(0.0005)
    fadeOut(red3, 0.0002)
    time.sleep(0.0005)
    fadeOut(red4, 0.0002)
    time.sleep(0.0005)
    fadeOut(red5, 0.0002)
    time.sleep(0.0005)
    fadeOut(red6, 0.0002)
    time.sleep(0.0005)
    fadeOut(red7, 0.0002)
    time.sleep(0.0005)
    fadeOut(red8, 0.0002)
    time.sleep(0.0005)

GPIO.setup("P9_41", GPIO.LOW)

for k in a:
    PWM.set_duty_cycle(red1, k)
    PWM.set_duty_cycle(red2, k)
    PWM.set_duty_cycle(red3, k)
    PWM.set_duty_cycle(red4, k)
    PWM.set_duty_cycle(red5, k)
    PWM.set_duty_cycle(red6, k)
    PWM.set_duty_cycle(red7, k)
    PWM.set_duty_cycle(red8, k)
    time.sleep(0.004)

GPIO.setup("P9_41", GPIO.HIGH)

for k in a:
    PWM.set_duty_cycle(red1, k)
    PWM.set_duty_cycle(red2, k)
    PWM.set_duty_cycle(red3, k)
    PWM.set_duty_cycle(red4, k)
    PWM.set_duty_cycle(red5, k)
    PWM.set_duty_cycle(red6, k)
    PWM.set_duty_cycle(red7, k)
    PWM.set_duty_cycle(red8, k)
    time.sleep(0.004)

GPIO.setup("P9_41", GPIO.LOW)

time.sleep(0.05)

for k in a:
    PWM.set_duty_cycle(red1, k)
    PWM.set_duty_cycle(red2, k)
    PWM.set_duty_cycle(red3, k)
    PWM.set_duty_cycle(red4, k)
    PWM.set_duty_cycle(red5, k)
    PWM.set_duty_cycle(red6, k)
    PWM.set_duty_cycle(red7, k)
    time.sleep(0.004)

GPIO.setup("P9_41", GPIO.HIGH)

for k in a:
    PWM.set_duty_cycle(red1, k)
    PWM.set_duty_cycle(red2, k)
    PWM.set_duty_cycle(red3, k)
    PWM.set_duty_cycle(red4, k)
    PWM.set_duty_cycle(red5, k)
    PWM.set_duty_cycle(red6, k)
    PWM.set_duty_cycle(red7, k)
    PWM.set_duty_cycle(red8, k)
    time.sleep(0.004)

GPIO.setup("P9_41", GPIO.LOW)
time.sleep(0.05)


for n in range(2):
    fadeIn(red1, 0.0001)
    time.sleep(0.00003)
    fadeIn(red2, 0.0001)
    time.sleep(0.00003)
    fadeIn(red3, 0.0001)
    time.sleep(0.00003)
    fadeIn(red4, 0.0001)
    time.sleep(0.00003)
    fadeIn(red5, 0.0001)
    time.sleep(0.00003)
    fadeIn(red6, 0.0001)
    time.sleep(0.00003)
    fadeIn(red7, 0.0001)
    time.sleep(0.00003)
    fadeIn(red8, 0.0001)
    fadeOut(red1, 0.0001)
    time.sleep(0.00003)
    fadeOut(red2, 0.0001)
    time.sleep(0.00003)
    fadeOut(red3, 0.0001)
    time.sleep(0.00003)
    fadeOut(red4, 0.0001)
    time.sleep(0.00003)
    fadeOut(red5, 0.0001)
    time.sleep(0.00003)
    fadeOut(red6, 0.0001)
    time.sleep(0.00003)
    fadeOut(red7, 0.0001)
    time.sleep(0.00003)
    fadeOut(red8, 0.0001)
    time.sleep(0.00003)

for l in range(2):
    fadeIn(red8, 0.0001)
    time.sleep(0.00003)
    fadeIn(red7, 0.0001)
    time.sleep(0.00003)
    fadeIn(red6, 0.0001)
    time.sleep(0.00003)
    fadeIn(red5, 0.0001)
    time.sleep(0.00003)
    fadeIn(red4, 0.0001)
    time.sleep(0.00003)
    fadeIn(red3, 0.0001)
    time.sleep(0.00003)
    fadeIn(red2, 0.0001)
    time.sleep(0.00003)
    fadeIn(red1, 0.0001)
    fadeOut(red8, 0.0001)
    time.sleep(0.00003)
    fadeOut(red7, 0.0001)
    time.sleep(0.00003)
    fadeOut(red6, 0.0001)
    time.sleep(0.00003)
    fadeOut(red5, 0.0001)
    time.sleep(0.00003)
    fadeOut(red4, 0.0001)
    time.sleep(0.00003)
    fadeOut(red3, 0.0001)
    time.sleep(0.00003)
    fadeOut(red2, 0.0001)
    time.sleep(0.00003)
    fadeOut(red1, 0.0001)
    time.sleep(0.00003)


# Now blink 3 times
for j in range(3):
    GPIO.setup("P9_41", GPIO.HIGH)
    PWM.set_duty_cycle(red1, 0)
    PWM.set_duty_cycle(red2, 0)
    PWM.set_duty_cycle(red3, 0)
    PWM.set_duty_cycle(red4, 0)
    PWM.set_duty_cycle(red5, 0)
    PWM.set_duty_cycle(red6, 0)
    PWM.set_duty_cycle(red7, 0)
    PWM.set_duty_cycle(red8, 0)

    time.sleep(0.3)
    GPIO.setup("P9_41", GPIO.LOW)
    PWM.set_duty_cycle(red8, 100)
    PWM.set_duty_cycle(red7, 100)
    PWM.set_duty_cycle(red6, 100)
    PWM.set_duty_cycle(red5, 100)
    PWM.set_duty_cycle(red4, 100)
    PWM.set_duty_cycle(red3, 100)
    PWM.set_duty_cycle(red2, 100)
    PWM.set_duty_cycle(red1, 100)
    time.sleep(0.3)

GPIO.setup("P9_41", GPIO.LOW)

for n in range(6):
    fadeIn(red1, 0.00004)
    time.sleep(0.00001)
    fadeIn(red2, 0.00004)
    time.sleep(0.00001)
    fadeIn(red3, 0.00004)
    time.sleep(0.00001)
    fadeIn(red4, 0.00004)
    time.sleep(0.00001)
    fadeIn(red5, 0.00004)
    time.sleep(0.00001)
    fadeIn(red6, 0.00004)
    time.sleep(0.00001)
    fadeIn(red7, 0.00004)
    time.sleep(0.00001)
    fadeIn(red8, 0.00004)
    fadeOut(red1, 0.00004)
    time.sleep(0.00001)
    fadeOut(red2, 0.00004)
    time.sleep(0.00001)
    fadeOut(red3, 0.00004)
    time.sleep(0.00001)
    fadeOut(red4, 0.00004)
    time.sleep(0.00001)
    fadeOut(red5, 0.00004)
    time.sleep(0.00001)
    fadeOut(red6, 0.00004)
    time.sleep(0.00001)
    fadeOut(red7, 0.00004)
    time.sleep(0.00001)
    fadeOut(red8, 0.00004)
    time.sleep(0.00001)

GPIO.setup("P9_41", GPIO.HIGH)

for l in range(6):
    fadeIn(red8, 0.00004)
    time.sleep(0.00001)
    fadeIn(red7, 0.00004)
    time.sleep(0.00001)
    fadeIn(red6, 0.00004)
    time.sleep(0.00001)
    fadeIn(red5, 0.00004)
    time.sleep(0.00001)
    fadeIn(red4, 0.00004)
    time.sleep(0.00001)
    fadeIn(red3, 0.00004)
    time.sleep(0.00001)
    fadeIn(red2, 0.00004)
    time.sleep(0.00001)
    fadeIn(red1, 0.00004)
    fadeOut(red8, 0.00004)
    time.sleep(0.00001)
    fadeOut(red7, 0.00004)
    time.sleep(0.00001)
    fadeOut(red6, 0.00004)
    time.sleep(0.00001)
    fadeOut(red5, 0.00004)
    time.sleep(0.00001)
    fadeOut(red4, 0.00004)
    time.sleep(0.00001)
    fadeOut(red3, 0.00004)
    time.sleep(0.00001)
    fadeOut(red2, 0.00004)
    time.sleep(0.00001)
    fadeOut(red1, 0.00004)
    time.sleep(0.00001)

GPIO.setup("P9_41", GPIO.LOW)

for k in a:
    PWM.set_duty_cycle(red1, k)
    PWM.set_duty_cycle(red2, k)
    PWM.set_duty_cycle(red3, k)
    PWM.set_duty_cycle(red4, k)
    PWM.set_duty_cycle(red5, k)
    PWM.set_duty_cycle(red6, k)
    PWM.set_duty_cycle(red7, k)
    PWM.set_duty_cycle(red8, k)
    time.sleep(0.004)

GPIO.setup("P9_41", GPIO.HIGH)

for k in a:
    PWM.set_duty_cycle(red1, k)
    PWM.set_duty_cycle(red2, k)
    PWM.set_duty_cycle(red3, k)
    PWM.set_duty_cycle(red4, k)
    PWM.set_duty_cycle(red5, k)
    PWM.set_duty_cycle(red6, k)
    PWM.set_duty_cycle(red7, k)
    PWM.set_duty_cycle(red8, k)
    time.sleep(0.004)

GPIO.setup("P9_41", GPIO.LOW)
time.sleep(0.3)
GPIO.setup("P9_41", GPIO.HIGH)
for k in a:
    PWM.set_duty_cycle(red1, k)
    PWM.set_duty_cycle(red2, k)
    PWM.set_duty_cycle(red3, k)
    PWM.set_duty_cycle(red4, k)
    PWM.set_duty_cycle(red5, k)
    PWM.set_duty_cycle(red6, k)
    PWM.set_duty_cycle(red7, k)
    PWM.set_duty_cycle(red8, k)
    time.sleep(0.004)



time.sleep(0.05)
GPIO.setup("P9_41", GPIO.LOW)


PWM.start(red1, 0)
PWM.start(red2, 0)
PWM.start(red3, 0)
PWM.start(red4, 0)
PWM.start(red5, 0)
PWM.start(red6, 0)
PWM.start(red7, 0)
PWM.start(red8, 0)


