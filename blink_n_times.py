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

# ITER_COUNT = args.num  

print(f"Blinking {args.num} times...")
sleep(0.5)

# while ITER_COUNT > 0:
#    ITER_COUNT -= 1
#    GPIO.output(pin1, GPIO.HIGH)
#    sleep(1)
#    GPIO.output(pin1, GPIO.LOW)
#    sleep(1)

for i in range(args.num):
    GPIO.output(pin1, GPIO.HIGH)
    sleep(1)
    GPIO.output(pin1, GPIO.LOW)
    sleep(1)

print("Done!")
GPIO.cleanup()
