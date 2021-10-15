#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

GPIO.output(17, GPIO.HIGH)
sleep(5)
GPIO.output(17, GPIO.LOW)
sleep(2)

GPIO.cleanup()
