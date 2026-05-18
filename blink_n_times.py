import sys  
import argparse
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

parser = argparse.ArgumentParser(description="Blink an LED n times")
parser.add_argument("--num", type=int, default=5, help="Number of times to blink")
args = parser.parse_args()

pin1 = 11
GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)

pin2 = 16  # buzzer
GPIO.setup(pin2, GPIO.OUT, initial=GPIO.LOW)


 
print(f"Blinking {args.num} times...")
sleep(1)

for i in range(args.num):
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.HIGH)
    sleep(1)
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)
    sleep(1)

print("Done!")
GPIO.cleanup()
