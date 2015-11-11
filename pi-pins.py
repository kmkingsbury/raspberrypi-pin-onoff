import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 


mypin = 18

GPIO.setup(mypin, GPIO.OUT)
GPIO.output(mypin, GPIO.HIGH)

runner = True

try:
    while (runner == True):
      time.sleep(1) #set to whatever

except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."    
    runner = False

GPIO.output(mypin, GPIO.LOW)
GPIO.cleanup()


