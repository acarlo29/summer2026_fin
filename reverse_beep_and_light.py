# Ultrasonic Sensor + LED
# Raspberry Pi GPIO

import RPi.GPIO as GPIO
import time

# Pins
# TRIG = 16
# ECHO = 18
# LED = 40

TRIG = 23
ECHO = 24
LED = 21
BUZZER = 26


GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

# buzzer set up
GPIO.setup(BUZZER, GPIO.OUT)

buzzer = GPIO.PWM(BUZZER, 1000)  # 1000 Hz tone
buzzer.start(0)                  # start silent

GPIO.output(TRIG, False)

time.sleep(2)

def get_distance():
    GPIO.output(TRIG, True)
    buzzer.ChangeDutyCycle(50)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    buzzer.ChangeDutyCycle(0)

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

        if dist < 10:
            GPIO.output(LED, True)
            buzzer.ChangeDutyCycle(50)
            time.sleep(0.1)
            GPIO.output(LED, False)
            buzzer.ChangeDutyCycle(0)
            time.sleep(0.1)

        elif dist < 25:
            GPIO.output(LED, True)
            buzzer.ChangeDutyCycle(50)
            time.sleep(0.2)
            GPIO.output(LED, False)
            buzzer.ChangeDutyCycle(0)
            time.sleep(0.2)

        elif dist < 35:
            GPIO.output(LED, True)
            buzzer.ChangeDutyCycle(50)
            time.sleep(0.35)
            GPIO.output(LED, False)
            buzzer.ChangeDutyCycle(0)
            time.sleep(0.35)

        elif dist < 50:
            GPIO.output(LED, True)
            buzzer.ChangeDutyCycle(50)
            time.sleep(0.5)
            GPIO.output(LED, False)
            buzzer.ChangeDutyCycle(0)
            time.sleep(0.5)

        else:
            GPIO.output(LED, True)
            buzzer.ChangeDutyCycle(50)
            time.sleep(1)
            GPIO.output(LED, False)
            buzzer.ChangeDutyCycle(0)
            time.sleep(1)

except KeyboardInterrupt:        # ← this was missing
    print("Stopped")
    buzzer.ChangeDutyCycle(0)
    buzzer.stop()
    GPIO.cleanup()