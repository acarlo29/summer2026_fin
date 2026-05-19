# comment for code here
# please work

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

print("LED ON")
GPIO.output(40, True)
time.sleep(3)

print("LED OFF")
GPIO.output(40, False)

GPIO.cleanup()