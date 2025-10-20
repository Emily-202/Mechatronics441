import RPi.GPIO as GPIO
from shifter import Shifter
import random
import time

GPIO.setmode(GPIO.BCM)

s = Shifter(2,3,4)      # serial=2, latch=3, clock=4
timeStep = 0.05
ledNum = 8
position = 3            # start around middle

def ledPos(p):
    s.shiftByte(1 << p)

try:
    while True:
        ledPos(position)
        time.sleep(timeStep)

        step = random.choice([-1, 1])
        new_p = position + step

        # edge cases
        if new_p < 0:
            new_p = 0
        elif new_p > ledNum - 1:
            new_p = ledNum - 1

        position = new_p

except KeyboardInterrupt:
    print("\nExiting...")
    s.shiftByte(0)                 # shift out all zeros
    time.sleep(0.05)               # brief delay so latch pulse completes
    GPIO.cleanup()