import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Shifter:
    # Assign instance attributes
    def __init__(self, serialPin, clockPin, latchPin):
        
        self.serial = serialPin     # Instance attribute
        self.clock = clockPin       # Instance attribute
        self.latch = latchPin       # Instance attribute

        GPIO.setup(serialPin, GPIO.OUT)
        GPIO.setup(latchPin, GPIO.OUT, initial=0)       # start latch & clock low
        GPIO.setup(clockPin, GPIO.OUT, initial=0)

    # Ping/Toggle pin high then low
    def ping(p):
        GPIO.output(p, 1)          # ping the latch pin to send register to output
        time.sleep(0)
        GPIO.output(p, 0)

    # Shift out a byte to the shift register
    def shiftByte(self, b):
        for i in range(8):
            GPIO.output(self.serial, b & (1<<i))
            self.__ping(self.clock)        # ping the clock pin to shift register data
        self.__ping(self.latch)            # ping the latch pin to send register to output


try:
    s = Shifter(2, 3, 4)        # serial=2, clock=3, latch=4
    s.shiftByte(0b01100110)     # test pattern
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
except Exception as e:
    print("Error:", e)
    GPIO.cleanup()
