import os
import RPi.GPIO as GPIO
import time
import re
import sys, argparse

# Parse Args:
def mainargs(argv):
  parser = argparse.ArgumentParser(description='Turn pins on and off on a Raspberry Pi 2 B+.')
  parser.add_argument('-p', '--pins', type=str, nargs='+', required=False,
                   help='pins to turn on (comma separated, range of values, or combination of two. Ex: \'14,15-18, 20\')')
  args = parser.parse_args()
  return args

# Make sure pins are in valid range, or drop
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

# take comma separated and/or range and make array of pins
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

# Main
GPIO.setmode(GPIO.BCM)

args = mainargs(sys.argv[1:])

strpins = ''
# From command line flag or prompt
if args.pins:
  strpins =  ','.join(args.pins) # if any spaces, this will flatten it to 1 arg
  strpins = strpins.replace(",,", ",") # spaces will cause double comma, fixes it
  #print "STR: " + strpins
else:
  strpins = raw_input('Enter Pins (ex: 14,15-17,18)): ')

# parse, validate, sort ascending
pins = split_pins(strpins)
pins = validate(pins)
pins.sort();

print "Pins: " + '[%s]' % ', '.join(map(str, pins))

# Can take list so send list of pins to set HIGH:
# Main Action / Runner
GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.HIGH)

print "Running (Ctrl-C to quit)..."
runner = True
try:
    while (runner == True):
      time.sleep(1) #set to whatever

except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    runner = False

GPIO.output(pins, GPIO.LOW)

GPIO.cleanup()
