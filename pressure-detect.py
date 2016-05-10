#!/usr/bin/env python

import os
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

while True:
	print(GPIO.input(23))
	if (GPIO.input(23) == True):
		os.system('omxplayer -o local example.mp3 &')
		# os.system('mpg123 -q example.mp3 &')
	sleep(0.5);

