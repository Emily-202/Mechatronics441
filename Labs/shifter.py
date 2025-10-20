import RPi.GPIO as GPIO
import time

class Shifter:
    # Assign instance attributes
    def __init__(self, serialPin, latchPin, clockPin):
        
        self.serial = serialPin     # Instance attribute
        self.latch = latchPin       # Instance attribute
        self.clock = clockPin       # Instance attribute

        GPIO.setup(serialPin, GPIO.OUT)
        GPIO.setup(latchPin, GPIO.OUT)       # start latch & clock low
        GPIO.setup(clockPin, GPIO.OUT)

    # Ping/Toggle pin high then low
    def ping(self, p):
        GPIO.output(p, 1)          # ping the latch pin to send register to output
        GPIO.output(p, 0)

    # Shift out a byte to the shift register
    def shiftByte(self, b):
        for i in range(7, -1, -1):       # shift out 8 bits, MSB first
            GPIO.output(self.serial, b & (1<<i))
            self.ping(self.clock)        # ping the clock pin to shift register data
        self.ping(self.latch)            # ping the latch pin to send register to output


try:
    """
    s = Shifter(2, 3, 4)        # serial=2, clock=3, latch=4
    s.shiftByte(0b01100110)     # test pattern
    print("Pattern displayed.")
    """
    while True:
        pass
except Exception as e:
    print("Error:", e)
    
