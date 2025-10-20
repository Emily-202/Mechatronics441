import RPi.GPIO as GPIO
from shifter import Shifter
import random
import time

class Bug:
    def __init__(self, timestep=0.1, x=3, isWrapOn=False):
        self.timestep = timestep            # time between moves
        self.x = x                          # current LED position (0-7)
        self.isWrapOn = isWrapOn            # wrap around edges if True
        self.__shifter = Shifter(2, 3, 4)   # private Shifter instance
        self._running = False

    def _update_position(self):
        step = random.choice([-1, 1])
        new_x = self.x + step

        if self.isWrapOn:
            # wrap around edges
            new_x = new_x % 8
        else:
            # clamp to edges
            if new_x < 0:
                new_x = 0
            elif new_x > 7:
                new_x = 7

        self.x = new_x

    def start(self):
        # Start moving the LED
        self._running = True
        try:
            while self._running:
                # update the display
                self.__shifter.shiftByte(1 << self.x)
                time.sleep(self.timestep)
                # compute next position
                self._update_position()
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        # Stop moving the LED and turn off the display
        self._running = False
        self.__shifter.shiftByte(0)  # turn off all LEDs
