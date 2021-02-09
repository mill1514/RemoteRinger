#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import logging

BELL_RELAY = 27                         
RING_TRIGGER_LENGTH = .050
RING_DELAY = 2.5
logging.basicConfig(filename='bell_cron.log', format=' %(message)s %(asctime)s', datefmt='%I:%M:%S %p %m/%d/%Y', level=logging.DEBUG)

GPIO.setwarnings(False)         # Disable annoying warning mesages for GPIO
GPIO.setmode(GPIO.BCM)          # Set to use Boardcom (BCM) markings for port numbers.
GPIO.setup(BELL_RELAY, GPIO.OUT, initial=GPIO.HIGH)  # Set GPIO port 27 as output to trigger relay, default = not triggered  

i = 0
while i < 3:
    GPIO.output(BELL_RELAY, GPIO.LOW)   # Set GPIO pin output to trigger relay
    time.sleep(RING_TRIGGER_LENGTH)     # Keep GPIO pin up/triggered for time needed to r to allow time to pull dinger
    GPIO.output(BELL_RELAY, GPIO.HIGH)  # Set GPIO pin out to default, not-triggered
    time.sleep(RING_DELAY)              # Delay between multiple rings
    i += 1
    
logging.info(" Bell rung from cronjob tre:  ")

GPIO.cleanup()                      # GPIO cleanup for a clean exit (reset ports used)

