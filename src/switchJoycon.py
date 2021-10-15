#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import RPi.GPIO as GPIO
import time
import pygame
import os

os.putenv('SDL_FBDEV', '/dev/fb0')

pygame.init()
joys = pygame.joystick.Joystick(0)
joys.init()


while True:
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYHATMOTION:
      print(event)
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(4, GPIO.OUT)
      GPIO.output(4, 1)
      time.sleep(2)
      GPIO.output(4, 0)
      time.sleep(1)
      GPIO.cleanup()
    else:
      print(event)

  time.sleep(0.1) 
