import RPi.GPIO as GPIO
import time

buzzer = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 440)
pwm.start(50)

def play_note(freq, duration):
    pwm.ChangeFrequency(freq)
    pwm.ChangeDutyCycle(50)
    time.sleep(duration * 0.8)
    pwm.ChangeDutyCycle(0)
    time.sleep(duration * 0.2)

def rest(duration):
    pwm.ChangeDutyCycle(0)
    time.sleep(duration)

# Imperial March
a  = 440
f  = 349
cH = 523
eH = 659
gH = 784
fH = 698
gS = 415

play_note(a, 0.5)
play_note(a, 0.5)
play_note(a, 0.5)
play_note(f, 0.35)
play_note(cH, 0.15)

play_note(a, 0.5)
play_note(f, 0.35)
play_note(cH, 0.15)
play_note(a, 1.0)

play_note(eH, 0.5)
play_note(eH, 0.5)
play_note(eH, 0.5)
play_note(fH, 0.35)
play_note(cH, 0.15)

play_note(gS, 0.5)
play_note(f, 0.35)
play_note(cH, 0.15)
play_note(a, 1.0)

pwm.stop()
time.sleep(0.1)
try:
    GPIO.cleanup()
except:
    pass