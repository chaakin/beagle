import Adafruit_BBIO.PWM as PWM
 
servo_pin = "P8_13"
duty_min = 2.5
duty_max = 13.1
duty_span = duty_max - duty_min
 
PWM.start(servo_pin, 100, 60.0)
 
while True:
    angle = raw_input("Angle (0 to 180 x to exit):")
    if angle == 'x':
        PWM.stop(servo_pin)
        PWM.cleanup()
        break
    angle_f = float(angle)
    print ('Angle_f=%s' % str(angle_f))
    duty = ((angle_f / 180) * duty_span + duty_min)
    print ('Doodie=%s' % str(duty))
    print "Setting duty to %.2f%%" % duty
    PWM.set_duty_cycle(servo_pin, duty)
