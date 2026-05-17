import sys  
import argparse
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library 
from time import sleep     # Import the sleep from time module 
GPIO.setwarnings(False)    # Ignore warning for now 
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering 

parser = argparse.ArgumentParser(description="Blink an LED n times")
parser.add_argument("--num", type=int, default=5, help="Number of times to blink")
args = parser.parse_args()


pin1 = 11 

ITER_COUNT = args.num()  

while ITER_COUNT > 0: # Run ITER_COUNT times 
   ITER_COUNT -= 1 # Decrement counter 
   GPIO.output(pin1, GPIO.HIGH) # Turn on 
   sleep(1)                     # Sleep for 1 second 
   GPIO.output(pin1, GPIO.LOW)  # Turn off 
   sleep(1)                     # Sleep for 1 second 

GPIO.cleanup() 