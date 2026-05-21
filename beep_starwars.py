import RPi.GPIO as GPIO
import time

buzzer = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 440)
pwm.start(50)

def play_note(freq, duration):
    if freq == 0:
        pwm.ChangeDutyCycle(0)
    else:
        pwm.ChangeFrequency(freq)
        pwm.ChangeDutyCycle(50)
    time.sleep(duration * 0.9)
    pwm.ChangeDutyCycle(0)
    time.sleep(duration * 0.1)

# Note frequencies
A4  = 440
F4  = 349
C5  = 523
E5  = 659
F5  = 698
A5  = 880
GS5 = 831
G5  = 784
DS5 = 622
D5  = 587
CS5 = 554
C5  = 523
B4  = 494
GS4 = 415
REST = 0

BPM = 120
Q = 60 / BPM        # quarter note
E = Q / 2           # eighth
S = Q / 4           # sixteenth
DQ = Q * 1.5        # dotted quarter
DE = E * 1.5        # dotted eighth
H = Q * 2           # half note

def play_imperial_march():
    # Phrase 1
    play_note(A4, DQ); play_note(A4, DQ)
    play_note(A4, S); play_note(A4, S); play_note(A4, S); play_note(A4, S)
    play_note(F4, E); play_note(REST, E)

    play_note(A4, DQ); play_note(A4, DQ)
    play_note(A4, S); play_note(A4, S); play_note(A4, S); play_note(A4, S)
    play_note(F4, E); play_note(REST, E)

    # Phrase 2
    play_note(A4, Q); play_note(A4, Q); play_note(A4, Q)
    play_note(F4, DE); play_note(C5, S)
    play_note(A4, Q); play_note(F4, DE); play_note(C5, S); play_note(A4, H)

    # Phrase 3
    play_note(E5, Q); play_note(E5, Q); play_note(E5, Q)
    play_note(F5, DE); play_note(C5, S)
    play_note(A4, Q); play_note(F4, DE); play_note(C5, S); play_note(A4, H)

    # Phrase 4 (the high bit)
    play_note(A5, Q); play_note(A4, DE); play_note(A4, S)
    play_note(A5, Q); play_note(GS5, DE); play_note(G5, S)
    play_note(DS5, S); play_note(D5, S); play_note(DS5, E)
    play_note(REST, E); play_note(A4, E)
    play_note(DS5, Q); play_note(D5, DE); play_note(CS5, S)

    play_note(C5, S); play_note(B4, S); play_note(C5, S)
    play_note(REST, E); play_note(F4, E)
    play_note(GS4, Q); play_note(F4, DE); play_note(A4, S)
    play_note(C5, Q); play_note(A4, DE); play_note(C5, S); play_note(E5, H)

    # Repeat phrase 4
    play_note(A5, Q); play_note(A4, DE); play_note(A4, S)
    play_note(A5, Q); play_note(GS5, DE); play_note(G5, S)
    play_note(DS5, S); play_note(D5, S); play_note(DS5, E)
    play_note(REST, E); play_note(A4, E)
    play_note(DS5, Q); play_note(D5, DE); play_note(CS5, S)

    play_note(C5, S); play_note(B4, S); play_note(C5, S)
    play_note(REST, E); play_note(F4, E)
    play_note(GS4, Q); play_note(F4, DE); play_note(A4, S)
    play_note(A4, Q); play_note(F4, DE); play_note(C5, S); play_note(A4, H)

for i in range(3):
    play_imperial_march()
    time.sleep(0.5)

pwm.stop()
time.sleep(0.1)
try:
    GPIO.cleanup()
except:
    pass