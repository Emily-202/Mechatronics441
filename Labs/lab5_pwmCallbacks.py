import RPi.GPIO as GPIO
import time
import math

## Setup ----------------------------------------------------------------

ledPins = [2, 3, 4, 14, 15, 18, 17, 27, 22, 23]    # adjust to your wiring
switch = 25                                        # button GPIO
baseFreq = 500                                     # 500 Hz base PWM
f = 0.2                                            # LED brightness wave frequency
phi = math.pi / 11                                 # phase difference between LEDs

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup LEDs
pwms = []
for pin in ledPins:
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, baseFreq)
    pwm.start(0)
    pwms.append(pwm)

# Setup button (active-high with pull-down)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


## Main Loop -------------------------------------------------------------

direction = 1   # +1 = forward, -1 = reverse
last_button_state = GPIO.input(switch)
t0 = time.time()

print("Running LED wave. Press Ctrl+C to exit.")
try:
    while True:
        t = time.time() - t0
        
        # --- Check for button press (edge detection manually) ---
        current_state = GPIO.input(switch)
        if current_state == GPIO.HIGH and last_button_state == GPIO.LOW:
            direction *= -1
            print(f"Direction changed! Now: {'Forward' if direction == 1 else 'Reverse'}")
            # small debounce delay
        last_button_state = current_state

        # --- Update LED brightness ---
        for i in range(len(pwms)):
            phi = direction * i * phi
            brightness = (math.sin(2 * math.pi * f * t - phi)) ** 2
            duty_cycle = brightness * 100
            pwms[i].ChangeDutyCycle(duty_cycle)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    for pwm in pwms:
        pwm.stop()
    GPIO.cleanup()
