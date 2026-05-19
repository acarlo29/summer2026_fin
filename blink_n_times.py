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

# pin2 = 16  # buzzer
# GPIO.setup(pin2, GPIO.OUT, initial=GPIO.LOW)

# pin2 = 16
pin2 = 39
GPIO.setup(pin2, GPIO.OUT, initial=GPIO.LOW)
buzzer = GPIO.PWM(pin2, 1000)  # 1000 Hz = typical beep tone


 
print(f"Blinking {args.num} times...")
sleep(1)

for i in range(args.num):
    GPIO.output(pin1, GPIO.HIGH)
    buzzer.start(50)   # 50% duty cycle = beep
    sleep(1)
    GPIO.output(pin1, GPIO.LOW)
    buzzer.stop()
    sleep(1)

print("Done!")

buzzer.stop()
GPIO.cleanup()

