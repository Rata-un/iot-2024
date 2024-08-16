import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
RED =  17
GREEN = 27
BLUE = 22
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)

while True:
	GPIO.output(RED,False)
	GPIO.output(GREEN,True)
	GPIO.output(BLUE,True)
	time.sleep(1)

	GPIO.output(RED,True)
	GPIO.output(GREEN,False)
	GPIO.output(BLUE,True)
	time.sleep(1)

	GPIO.output(RED,True)
	GPIO.output(GREEN,True)
	GPIO.output(BLUE, False)
	time.sleep(1)

	GPIO.output(RED,False)
	GPIO.output(BLUE,False)
	GPIO.output(GREEN,True)
	time.sleep(1)

	GPIO.output(RED,False)
	GPIO.output(GREEN,True)
	GPIO.output(BLUE, False)
	time.sleep(1)

	GPIO.output(RED,True)
	GPIO.output(GREEN,False)
	GPIO.output(BLUE,False)
	time.sleep(1)

	GPIO.output(RED,False)
	GPIO.output(GREEN,False)
	GPIO.output(BLUE, False)
	time.sleep(1)
