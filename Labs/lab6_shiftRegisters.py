import RPi.GPIO as GPIO
from shifter import Shifter
import time

s = Shifter(2,3,4)
s.shiftByte(0b10101010)
time.sleep(2)
s.shiftByte(0b01010101)
time.sleep(2)
s.shiftByte(0)
GPIO.cleanup()