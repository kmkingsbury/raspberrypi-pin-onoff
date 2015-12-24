import os
import RPi.GPIO as GPIO
import time
import re

def validate(inpins):
    outpins = []
    #2 to 27 is valid pin numbers
    for (i,item) in enumerate(inpins):
        #print "Checking: " + str(item)
        if int(item) < 2 or int(item) > 27:
            print "Item " + str(item) + " is not valid, removing."
        else:
            outpins.append(int(item))
    return outpins

def split_pins(inpins):
  listout = []
  list1 = inpins.split(',')
  for item in list1:
    #print "item: " + str(item)
    if re.search('-', item):
        r = item.split('-')
        #print "match in "+ item
        for num in range(int(r[0]),int(r[1])+1):
            #print "R:"+ str(num)
            listout.append(int(num))
    else:
        #print "no match " + item
        listout.append(int(item))
  return listout
GPIO.setmode(GPIO.BCM)


strpins = raw_input('Enter Pins (ex: 14,15-17,18))')

pins = split_pins(strpins)
pins = validate(pins)
pins.sort();

print "Pins: "
print '[%s]' % ', '.join(map(str, pins))

# Can take list so send list of pins to set HIGH:
#for mypin in listpins:
# print "Setting: " + str(mypin)
GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.HIGH)

runner = True
try:
    while (runner == True):
      time.sleep(1) #set to whatever

except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    runner = False

GPIO.output(pins, GPIO.LOW)

GPIO.cleanup()
