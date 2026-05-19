import argparse
import RPi.GPIO as GPIO
from time import sleep, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

TRIG = 18
ECHO = 22

GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    # Send trigger pulse
    GPIO.output(TRIG, GPIO.HIGH)
    sleep(0.00001)  # 10 microseconds
    GPIO.output(TRIG, GPIO.LOW)

    # Wait for echo to start
    while GPIO.input(ECHO) == 0:
        pulse_start = time()