import RPi.GPIO as GPIO
import time
from bugClass import Bug

# Setup GPIO mode FIRST
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO input pins for switches
s1 = 17  # switch 1: turn bug on/off
s2 = 27  # switch 2: toggle wrap
s3 = 22  # switch 3: speed boost

# Setup GPIO inputs
GPIO.setup(s1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Instantiate Bug
bug = Bug()

# Track previous states
originalSpeed = bug.timestep
prev_s2 = GPIO.input(s2)
prev_s3 = GPIO.input(s3)
bug_active = False

try:
    while True:
        # Read the switches
        s1_state = GPIO.input(s1)
        s2_state = GPIO.input(s2)
        s3_state = GPIO.input(s3)

        # Bug on/off
        if s1_state and not bug_active:
            # Start moving
            bug._running = True
            bug_active = True
            print("Bug started")
        elif not s1_state and bug_active:
            # Stop moving and turn off display
            bug._running = False
            bug._Bug__shifter.shiftByte(0)  # Turn off LEDs
            bug_active = False
            print("Bug stopped")

        # Wrapping changes (Toggle)
        if s2_state != prev_s2 and s2_state:
            bug.isWrapOn = not bug.isWrapOn
            print(f"Wrap: {'ON' if bug.isWrapOn else 'OFF'}")
        prev_s2 = s2_state

        # Speed changes
        if s3_state:
            bug.timestep = originalSpeed / 3  # speed up 3x
        else:
            bug.timestep = originalSpeed      # normal speed

        if prev_s3 != s3_state and s3_state:
            print(f"Speed: 3x")
        elif prev_s3 != s3_state and not s3_state:
            print(f"Speed: 1x")
        prev_s3 = s3_state

        # If bug is active, update its position and display
        if bug_active:
            bug._update_position()
            bug._Bug__shifter.shiftByte(1 << bug.x)



except KeyboardInterrupt:
    print("\nExiting...")
finally:
    # Clean up
    bug._running = False
    bug._Bug__shifter.shiftByte(0)  # Turn off LEDs
    GPIO.cleanup()
    print("GPIO cleaned up")