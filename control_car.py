import Adafruit_BBIO.PWM as PWM
import time
import sys
 
servo_pin = "P8_13"
duty_min = 2.5
duty_max = 13.1
duty_span = duty_max - duty_min
 
PWM.start(servo_pin, duty_span * 0.5, 60.0)
time.sleep(3)
PWM.set_duty_cycle(servo_pin, 8.38888888889)
time.sleep(5)




PWM.stop(servo_pin)
PWM.cleanup()
sys.exit(0)
