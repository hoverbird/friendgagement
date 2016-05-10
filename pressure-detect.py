#!/usr/bin/env python

import os
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

while True:
	if (GPIO.input(23) == False):
		os.system('omxplayer -o local example.mp3 &')

	sleep(0.1);

