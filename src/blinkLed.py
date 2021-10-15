#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

for i in range(5):
  GPIO.output(17, GPIO.HIGH)
  sleep(0.5)
  GPIO.output(17, GPIO.LOW)
  sleep(0.5)

else:
  GPIO.cleanup()
