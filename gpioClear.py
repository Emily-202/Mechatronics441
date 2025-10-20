import sys
import argparse

#!/usr/bin/env python3
"""
gpioClear.py

Set specified Raspberry Pi GPIO pins LOW (clear) and optionally clean up.
Usage:
    sudo python3 gpioClear.py -p 17 18 27         # BCM mode (default)
    sudo python3 gpioClear.py --mode BOARD -p 11 13
    sudo python3 gpioClear.py -p 17 --no-cleanup  # leave pins configured low
"""


try:
        import RPi.GPIO as GPIO
except Exception as e:
        sys.exit("RPi.GPIO not available. Run on a Raspberry Pi with RPi.GPIO installed.")

def clear_pins(pins, mode, do_cleanup):
        if mode.upper() == "BOARD":
                GPIO.setmode(GPIO.BOARD)
        else:
                GPIO.setmode(GPIO.BCM)

        GPIO.setwarnings(False)

        for p in pins:
                GPIO.setup(p, GPIO.OUT, initial=GPIO.LOW)

        # ensure outputs have settled
        GPIO.output(pins, GPIO.LOW)

        if do_cleanup:
                # cleanup will reset pin modes (may float them)
                GPIO.cleanup()

def parse_pins(pin_args):
        pins = []
        for item in pin_args:
                # allow comma-separated or space separated values
                for tok in str(item).split(","):
                        tok = tok.strip()
                        if not tok:
                                continue
                        try:
                                pins.append(int(tok))
                        except ValueError:
                                sys.exit(f"Invalid pin value: {tok}")
        if not pins:
                sys.exit("No GPIO pins specified. Use -p/--pins to provide a list.")
        return pins

def main():
        parser = argparse.ArgumentParser(description="Clear (set LOW) Raspberry Pi GPIO pins.")
        parser.add_argument("-p", "--pins", nargs="+", required=True,
                                                help="Pins to clear. Use BCM or BOARD numbers. Accepts space or comma separated values.")
        parser.add_argument("--mode", choices=["BCM", "BOARD"], default="BCM",
                                                help="Pin numbering mode (default: BCM).")
        parser.add_argument("--no-cleanup", dest="cleanup", action="store_false",
                                                help="Do not call GPIO.cleanup() after clearing pins (leave as outputs LOW).")
        args = parser.parse_args()

        pins = parse_pins(args.pins)
        try:
                clear_pins(pins, args.mode, args.cleanup)
        except Exception as e:
                sys.exit(f"Error manipulating GPIO: {e}")

if __name__ == "__main__":
        main()