# Ultrasonic Sensor + LED
# Raspberry Pi GPIO

import RPi.GPIO as GPIO
import time

# Pins
TRIG = 16
ECHO = 18
LED = 40  # your LED pin

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(TRIG, False)

time.sleep(2)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = round(pulse_duration * 17150, 2)
    return distance

try:
    while True:
        dist = get_distance()
        print("Distance:", dist, "cm")

        # Very close = fast flashing
        if dist < 10:
            GPIO.output(LED, True)
            time.sleep(0.05)
            GPIO.output(LED, False)
            time.sleep(0.05)

        # Medium = slower flashing
        elif dist < 25:
            GPIO.output(LED, True)
            time.sleep(0.1)
            GPIO.output(LED, False)
            time.sleep(0.2)

        # Farther = slow flashing
        elif dist < 50:
            GPIO.output(LED, True)
            time.sleep(0.2)
            GPIO.output(LED, False)
            time.sleep(0.5)

        # Too far = LED off
        else:
             GPIO.output(LED, False)
