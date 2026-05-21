import RPi.GPIO as GPIO
import time

buzzer = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 440)
pwm.start(50)

melody = [
    392, 392, 392,
    311, 466, 392,
    311, 466, 392
]

durations = [
    0.4, 0.4, 0.4,
    0.3, 0.7, 0.4,
    0.3, 0.7, 0.6
]

for note, dur in zip(melody, durations):
    pwm.ChangeFrequency(note)
    time.sleep(dur)

pwm.stop()
GPIO.cleanup()