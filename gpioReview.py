import RPi.GPIO as GPIO # import RPi.GPIO module

GPIO.setmode(GPIO.BCM) # select BCM pin numbering
GPIO.setmode(GPIO.BOARD) # select BOARD pin numbering

# Set up inputs (p = port# or pin#)
# All GPIO pins default to *input* state
# Set pin as input:
GPIO.setup(p, GPIO.IN)
GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up outputs
GPIO.setup(p, GPIO.OUT)
GPIO.setup(p, GPIO.OUT, initial=1) # initial value 1 or 0

# Set output value
GPIO.output(p, 1) # set an output port/pin value to: 1 / GPIO.HIGH / True
GPIO.output(p, 0) # set an output port/pin value to: 0 / GPIO.LOW / False

# Read input (or output status) value
in = GPIO.input(p) # read status (0 or 1) of pin/port and assign to variable

# PWM
pwm = GPIO.PWM(p, frequency_Hz) # create a PWM object
pwm.start(duty_cycle) # set duty cycle (0.0 – 100.0)
pwm.ChangeFrequency(frequency_Hz) # change frequency (in Hz)
pwm.ChangeDutyCycle(duty_cycle) # change duty cycle (0.0 – 100.0)
pwm.stop() # stop the PWM object

# Detect rising or falling signal edge (blocking call)
GPIO.wait_for_edge(p, GPIO.RISING) # pause code until rising edge detected
GPIO.wait_for_edge(p, GPIO.FALLING) # pause code until falling edge detected

# Add a callback function to execute a new thread when
# edge rise or fall (or both/either) detected (non-blocking):
GPIO.add_event_detect(p, GPIO.RISING, callback=fn, bouncetime=t_ms)
GPIO.add_event_detect(p, GPIO.FALLING, callback=fn, bouncetime=t_ms)
GPIO.add_event_detect(p, GPIO.BOTH, callback=fn, bouncetime=t_ms)

# Remove a previously-defined callback function
GPIO.remove_event_detect(p)

# Clean up on exit
GPIO.cleanup()