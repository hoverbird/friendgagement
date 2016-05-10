#!/usr/bin/env python

import os
from time import sleep
from threading import Timer

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

templeActive = False

def deactivateTemple():
	print("Deactivating temple")
	templeActive = False

def activateTemple():
	print("Deactivating temple")
	templeActive = True


while True:
	print(templeActive)
	if (GPIO.input(23) == False and templeActive == False):	
		activateTemple()
		os.system('omxplayer -o local example.mp3 &')
		# os.system('mpg123 -q example.mp3 &')
                Timer(10.0, deactivateTemple).start()

	sleep(0.2);

