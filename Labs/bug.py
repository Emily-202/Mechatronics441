import RPi.GPIO as GPIO
import time
import threading
from lab6_shiftRegisters import Bug  # import the Bug class we just created

# GPIO input pins for switches
s1 = 17  # switch 1: turn bug on/off
s2 = 27  # switch 2: toggle wrap
s3 = 22  # switch 3: speed boost

# Setup GPIO inputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(s1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Instantiate Bug (default parameters)
bug = Bug()

# Thread to run the bug animation
bug_thread = threading.Thread(target=bug.start)
bug_thread.daemon = True  # will exit when main program exits
bug_thread.start()

# Track previous state of S2 to detect changes
prev_s2 = GPIO.input(s2)

try:
    while True:
        # Read the switches
        s1_state = GPIO.input(s1)
        s2_state = GPIO.input(s2)
        s3_state = GPIO.input(s3)

        # Bug on/off
        if s1_state:
            # Move the bug when on
            bug._update_position()          # compute next LED position
            bug._Bug__shifter.shiftByte(1 << bug.x)         # update display
        else:
            # Turn off display when off
            bug._Bug__shifter.shiftByte(0)

        # Wrapping changes
        if s2_state != prev_s2:
            bug.isWrapOn = not bug.isWrapOn
            prev_s2 = s2_state              # update previous state

        # Speed changes
        if s3_state:
            delay = bug.timestep / 3        # speed up 3x
        else:
            delay = bug.timestep

        # Wait before next loop iteration
        time.sleep(delay)

except KeyboardInterrupt:
    print("\nExiting...")
    bug.stop()