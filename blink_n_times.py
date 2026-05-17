import sys  
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pin1 = 11

# Get blink count from user
try:
    num_blinks = int(input("How many times should the LED blink? "))
    if num_blinks <= 0:
        print("Please enter a positive number. Defaulting to 5.")
        num_blinks = 5
except ValueError:
    print("Invalid input. Defaulting to 5 blinks.")