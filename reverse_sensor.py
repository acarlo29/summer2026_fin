# Ultrasonic Sensor + Active Buzzer
# Raspberry Pi GPIO

import RPi.GPIO as GPIO
import time

# Pins
TRIG = 16
ECHO = 18
BUZZER = 40

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

GPIO.output(TRIG, False)

time.sleep(2)

def get_distance():
    # Send pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Wait for echo start
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    # Wait for echo end
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    # Distance in cm
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

try:
    while True:
        dist = get_distance()
        print("Distance:", dist, "cm")

        # Very close = fast beeping
        if dist < 10:
            GPIO.output(BUZZER, True)
            time.sleep(0.05)
            GPIO.output(BUZZER, False)
            time.sleep(0.05)

        # Medium distance = slower beeping
        elif dist < 25:
            GPIO.output(BUZZER, True)
            time.sleep(0.1)
            GPIO.output(BUZZER, False)
            time.sleep(0.2)

        # Farther away = very slow beeping
        elif dist < 50:
            GPIO.output(BUZZER, True)
            time.sleep(0.2)
            GPIO.output(BUZZER, False)
            time.sleep(0.5)

        # Too far = no sound
        else:
            GPIO.output(BUZZER, False)
            time.sleep(0.3)

except KeyboardInterrupt:
    print("Stopped")
    GPIO.cleanup()