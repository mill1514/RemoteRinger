#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import logging

BELL_RELAY = 27                         
RING_TRIGGER_LENGTH = .050
logging.basicConfig(filename='./bell_cron.log', format=' %(message)s %(asctime)s', datefmt='%I:%M:%S %p %m/%d/%Y', level=logging.DEBUG)


GPIO.setwarnings(False)         # Disable annoying warning mesages for GPIO
GPIO.setmode(GPIO.BCM)          # Set to use Boardcom (BCM) markings for port numbers.
GPIO.setup(BELL_RELAY, GPIO.OUT, initial=GPIO.HIGH)  # Set GPIO port 27 as output to trigger relay, default = not triggered  

GPIO.output(BELL_RELAY, GPIO.LOW)   # Set GPIO pin output to trigger relay
time.sleep(RING_TRIGGER_LENGTH)     # Keep GPIO pin up/triggered for time needed to r to allow time to pull dinger
GPIO.output(BELL_RELAY, GPIO.HIGH)  # Set GPIO pin out to default, not-triggered
logging.info("Bell rung from cronjob uno:  ")


GPIO.cleanup()                      # GPIO cleanup for a clean exit (reset ports used)

