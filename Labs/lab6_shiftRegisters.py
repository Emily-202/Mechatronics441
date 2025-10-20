import RPi.GPIO as GPIO
from shifter import Shifter
import random
import time

s = Shifter(2,3,4)      # serial=2, clock=3, latch=4
timeStep = 0.05
ledNum = 8
position = 3            # start around middle

def ledPos(p):
    s.shiftByte(1 << p)

try:
    while True:
        ledPos(position)
        time.Sleep(timeStep)

        step = random.choice([-1, 1])
        new_p = position + step

        if new_p < 0:
            new_p = 0
        elif new_p > ledNum - 1:
            new_p = ledNum - 1

        position = new_p

except KeyboardInterrupt:
    print("\nExiting...")
    s.shiftByte(0b00000000)         # turn all LEDs off
    GPIO.cleanup()